# Django SF template
This is a template for a Django project that uses [poetry](https://python-poetry.org/), [python-webpack-boilerplate](https://github.com/AccordBox/python-webpack-boilerplate)  and [materializecss](https://materializecss.com/).

# Local Setup
You need to have [python](https://www.python.org/), [poetry](https://python-poetry.org/) and [npm](https://www.npmjs.com/) installed in your machine. 

1. create an `.env` file, with environment variables, like it's in `.env.example`;
2. Install dependencies with `poetry install`;
3. Launch a poetry shell so the dependencies are active: `poetry shell`;
4. Run `python manage.py migrate` to create the databases tables;
5. This version uses  [python-webpack-boilerplate](https://github.com/AccordBox/python-webpack-boilerplate) 
so we can use webpack for styling and packing javascript. Make sure you install the necessary dependencies:
   * `cd frontend` - change to frontend directory;
   * `npm install` - install the dependecies; 
   *  `npm run build` - creates a build directory with a production build of the files;
   *  To work more on the frontend, see instructions in the [frontend](./frontend/README.md) directory.
5. Go back to the main directory (`cd ..`) and run `python manage.py runserver 8000` to access the portal site.


# Docker Setup
If you have docker setup on your computer, you can run the following steps to get a local copy running:
   * `docker-compose build` - Build the images using the Dockerfile provided in this repo.
   * `docker-compose up` - Will spin up a copy of LW-NG along with a postgres database (at http://127.0.0.1:8000) as long as that address isn't taken by another service.

# DIY Instructions
You might want to start this from scratch in a new empty directory - You can find the full tutorial [here](https://digi-docs-bot.herokuapp.com/full-stack/SF-Django-Setup/)
