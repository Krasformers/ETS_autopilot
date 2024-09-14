FROM pytorch/pytorch:latest
RUN  apt-get -y update && apt-get -y full-upgrade
RUN  apt-get -y install git wget
RUN  git clone https://github.com/facebookresearch/segment-anything-2.git
WORKDIR /workspace/segment-anything-2/
RUN  pip install -e ".[demo]"
RUN  cd checkpoints && ./download_ckpts.sh && cd ..
COPY requirements.txt /requirements.txt
RUN  python3 -m pip install --upgrade pip --no-cache-dir --root-user-action=ignore
RUN  python3 -m pip install -r /requirements.txt --no-cache-dir --root-user-action=ignore
CMD  jupyter notebook --notebook-dir=/notebooks --ip=0.0.0.0 --port=9999 --no-browser --allow-root