# Contact Book RESTful API

This project is a simple API for managing contacts in a contact book. You can add, delete, retrieve, update contacts, and more.

## Requirements

- Python 3.8+
- Django
- Django REST Framework
- PostgreSQL (running in Docker, if necessary)
- Postman (for testing the API)

# Docker Configuration

This project uses Docker to manage the PostgreSQL database used for storing contact data. Docker allows for easy and consistent database setup across different environments.

## Requirements

Before using Docker, ensure that you have Docker and Docker Compose installed on your system. If not, you can download and install them from the official Docker website:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Drebedenb/contact-book.git
   cd contact-book
   ```
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
3. Run Docker (don't forget launch it before):

   ```bash
   docker-compose up -d
   ```
   
4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. Create a superuser for authentication:

   ```bash
   python manage.py createsuperuser
   ```
   
6. Create a superuser for authentication:

   ```bash
   python manage.py runserver
   ```
   
The application will be accessible at http://127.0.0.1:8000/.

# Usage

To interact with the API, you can use Postman or other tools. The API provides the following endpoints:

- **GET /api/v1/contacts/**: Get a list of all contacts.
- **POST /api/v1/contacts/**: Add a new contact.
- **GET /api/v1/contacts/\<id>/**: Get a contact by ID.
- **PUT /api/v1/contacts/\<id>/**: Update a contact by ID.
- **DELETE /api/v1/contacts/\<id>/**: Delete a contact by ID.


## Authentication
The API uses Basic Authentication. To authenticate, send a request with the superuser's credentials.
You can use Postman Authorization tab with Basic Auth selected in dropdown.

## Additional Features (Optional)
You can perform contact search by name or last name by adding query parameters.
Pagination for the list of contacts is enabled by default.

- **GET /api/v1/contacts/?first_name=<first_name>**: Search for contacts by first_name or last_name.
- **GET /api/v1/contacts/?offset=<page-number>**: Access a specific page of the contact list with pagination. 
The default count of subjects on one page is 2.


## Conclusion
You have successfully configured and launched the API for the contact book. You can now begin using it to manage contacts.

## License
This project is licensed under the MIT License.