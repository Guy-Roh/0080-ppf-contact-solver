MY_WEB_PORT=8080      # JupyterLab port on your side
MY_BLENDER_PORT=9090  # Solver port for the Blender add-on
IMAGE_NAME=ghcr.io/st-tech/ppf-contact-solver-compiled:latest
docker run --rm -it \
  --name ppf-contact-solver \
  --gpus all \
  -p ${MY_WEB_PORT}:${MY_WEB_PORT} \
  -p ${MY_BLENDER_PORT}:${MY_BLENDER_PORT} \
  -e WEB_PORT=${MY_WEB_PORT} \
  $IMAGE_NAME # Image size ~1GB
