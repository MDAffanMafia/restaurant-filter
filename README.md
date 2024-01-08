# Restaurant Search App

Welcome to the Restaurant Search App, a platform where users can explore and find information about various restaurants, their menus, and user reviews.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation


1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MDAffanMafia/restaurant-filter.git
   cd restaurant-search-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

Now you can access the project locally at 'http://localhost:8000'.

## Features

- **Search Dishes By Restaurants:** Users can search for dishes with  restaurants.
- **Search Dishes By Price:** Users can search for dishes with  price.

## Usage

1. Visit 'http://localhost:8000' in your web browser.
2. Explore restaurants using the search functionality.
3. Click on a restaurant to view its details, including menu and reviews.
4. Leave a review for a restaurant you've visited.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
6. Please adhere to the code style and formatting guidelines.

If you encounter any issues or have ideas for improvements, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
