# Ray Tracer
A Python implementation of the ray tracer based on [The Ray Tracer Challenge](http://raytracerchallenge.com/) (work in progress).

![Raytraced Image](images/sphere.png)

## Running the project
To run the main script, execute the following command from the project's root directory:
```bash
python3 -m raytracer.raytracer
```
## Testing
To format the code, perform static type checking, and run tests, use the following command:
```bash
black . && mypy . && pytest -v
```
- `black .` formats the code.
- `mypy .` checks for type consistency.
- `pytest -v` runs all tests in verbose mode.

## Profiling
```bash
python -m cProfile -o profile_output.prof -m raytracer.raytracer
snakeviz profile_output.prof
```
    
