# Example of BuildKit on CI
In this example, we create a multi-staged Dockerfile with a very simple Python script. Then we use buildkit (directly or via buildx) to build this Dockerfile.

> Feel free to use and modify the examples to your use case.

## CI Steps
- build-buildkit: will use BuildKit to build the image and publish it to the respective Container Registry.
- test-image: will run the image to see that everything is working properly.