# File: panel_colors.py
# Code: Claude Code and Codex
# Review: Ryoichi Ando (ryoichi.ando@zozo.com)
# License: Apache v2.0
#
# Generates a small solid-colour preview icon for each N-panel so that every
# panel header carries a distinct colour swatch to the left of its title.

import bpy  # pyright: ignore

_preview_collections: dict = {}

# Map each panel bl_idname → (R, G, B) in linear 0-1 range.
# Colours are chosen to be clearly distinct against Blender's default dark theme.
PANEL_COLORS: dict[str, tuple[float, float, float]] = {
    "MAIN_PT_RemotePanel":          (0.22, 0.52, 0.88),  # steel blue   – Backend Communicator
    "SSH_PT_SolverPanel":           (0.22, 0.75, 0.34),  # green        – Solver
    "SSH_PT_ObjectGroupsManager":   (0.92, 0.52, 0.12),  # orange       – Scene Configuration
    "DYNAMICS_PT_Groups":           (0.62, 0.28, 0.92),  # violet       – Dynamics Groups
    "SNAPMERGE_PT_SnapAndMerge":    (0.18, 0.76, 0.76),  # teal         – Snap and Merge
    "VISUALIZATION_PT_Visualization": (0.88, 0.82, 0.12),  # yellow     – Visualization
}

_ICON_SIZE = 16


def _make_icon(pcoll, key: str, rgb: tuple[float, float, float]) -> None:
    """Create a solid-colour square preview icon and store it in *pcoll*."""
    icon = pcoll.new(key)
    icon.image_size = (_ICON_SIZE, _ICON_SIZE)
    r, g, b = rgb
    icon.image_pixels_float = [r, g, b, 1.0] * (_ICON_SIZE * _ICON_SIZE)


def get_panel_icon_id(panel_bl_idname: str) -> int:
    """Return the Blender icon_id for *panel_bl_idname*, or 0 if not found."""
    pcoll = _preview_collections.get("panel_colors")
    if pcoll is None:
        return 0
    entry = pcoll.get(panel_bl_idname)
    return entry.icon_id if entry is not None else 0


def register() -> None:
    import bpy.utils.previews  # pyright: ignore
    pcoll = bpy.utils.previews.new()
    for idname, rgb in PANEL_COLORS.items():
        _make_icon(pcoll, idname, rgb)
    _preview_collections["panel_colors"] = pcoll


def unregister() -> None:
    import bpy.utils.previews  # pyright: ignore
    for pcoll in _preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    _preview_collections.clear()
