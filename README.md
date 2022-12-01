# Heart-Charity
 
 github-link - https://github.com/Suraj1089/Heart-Charity


## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [About Author](#about-author)
- [Gallery](#gallery)


## Description

This is a website for a charity organization. Users can connect with organisation and help each other. This website is made using HTML, CSS, JavaScript, Bootstrap, and Django.It includes features like payment gateway, contact form,recatpha validation and many more.

## Features

- Payment Gateway
- Contact Form
- User Authentication
- User dashboard
- Recapcha Validation
- Responsive Design
- Blogs


## Installation

- Clone the repository
```
git clone https://github.com/Suraj1089/Heart-Charity.git
```
- Install the requirements
```
pip install -r requirements.txt
```

- Database Setup
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Here, you can use any database you want. I have used sqlite3 database.

to know more about database setup, visit https://docs.djangoproject.com/en/3.2/ref/settings/#databases

```

- Migrate the database
```
python manage.py make migrations
python manage.py migrate

```

- Create a superuser
```
python manage.py createsuperuser

```

- Run the server
```
python manage.py runserver

```

## Usage

- You can use this website for any charity organization.
- remove media directory from .gitignore so uploaded images can be visible.


## Contributing

You can clone the repository and make changes to it. It is open for all.


## License

[MIT](https://choosealicense.com/licenses/mit/)

## About Author

<a href="https://github.com/Suraj1089" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>

<a href="https://linkedin.com/in/surajpisal" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
<a href="https://surajpisal.netlify.com" target="_blank">
<img src=https://img.shields.io/badge/-Portfolio-red alt=linkedin style="margin-bottom: 5px;width:80px" />
</a>

<a href="https://instagram.com/suraj_pisal9" target="_blank">
<img src=https://img.shields.io/badge/instagram-%23000000.svg?&style=for-the-badge&logo=instagram&logoColor=white alt=instagram style="margin-bottom: 5px;" />
</a>  

## Gallery
```
Home - http://127.0.0.1:8000/
```

![image](https://user-images.githubusercontent.com/85509795/205105466-2d1ad458-42b5-4abc-ac17-3287ff221446.png)

```
Voluteer Form  http://127.0.0.1:8000/

```
![image](https://user-images.githubusercontent.com/85509795/205106053-54dc1e97-793b-4787-8ad2-9fd976380b62.png)


```
User Registraion http://127.0.0.1:8000/auth/signup/

```
![image](https://user-images.githubusercontent.com/85509795/205106829-4119ac96-1a79-4679-8083-a7bfac0b1ca7.png)

```
User dashboard http://127.0.0.1:8000/auth/dashboard/

```
![image](https://user-images.githubusercontent.com/85509795/205108489-6ffb3ae8-c5c0-4106-827e-075504df6e40.png)

Images source - https://www.pexels.com/



