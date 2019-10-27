set -eu
docker build -f docker/Dockerfile -t integration_test .
docker run integration_test