from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from typing import List, Dict

# Create your views here.
power_of_django: List[Dict[str, str]] = [
    {'heading': 
        'The Power of Django: A Versatile Web Framework for Python'
     },
    
    {'introduction':'Django is a high-level web framework for Python that encourages rapid development and clean, pragmatic design. Built by experienced developers, Django takes care of much of the hassle of web development, allowing you to focus on writing your app without needing to reinvent the wheel. Its popularity has surged among developers due to its simplicity, flexibility, and a robust set of built-in features.'        
    },
    {
        'features':
            {
                'orm':"Django's ORM provides an abstraction layer, making database interactions seamless. You can interact with your database using Python code instead of writing raw SQL queries.",
            
                'automatic_admin_interface':"One of Django's standout features is its admin interface, which is automatically generated and allows for easy management of application data.",
                
                'template_Engine': "Django's template engine facilitates the generation of HTML dynamically. It allows you to separate the design from the business logic of the application.",
                
                'security': "Django provides strong built-in security features, including protection against common threats like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).",
                
                'scalability':"Django provides strong built-in security features, including protection against common threats like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF)."
            },
    },
    {
        'uses':
            {
                "web_Application": "Django is well-suited for developing complex web applications due to its comprehensive suite of tools. Examples include content management systems (CMS), social networks, and e-commerce platforms.",
                
                'api':"With Django REST framework, you can easily build robust and scalable APIs. This is particularly useful for mobile and single-page applications (SPAs) that need to interact with a backend server.",
                
                'prototyping': "Due to its rapid development capabilities, Django is an excellent choice for creating prototypes and minimum viable products (MVPs). This allows startups and businesses to test ideas quickly.",
                
                'data_Driven_Applications': "Django's ORM, combined with its data validation and handling capabilities, makes it ideal for applications that need to process and display large amounts of data, such as analytics dashboards.",
                
                'educational_Platforms': "Many educational institutions use Django to build platforms for online courses, student management systems, and learning tools."
            }
    },
    {
        'conclusion': "Django stands out as a powerful and flexible framework that enables developers to build dynamic and robust web applications. Its emphasis on 'don't repeat yourself' (DRY) principles and the availability of a wide range of built-in features make it an attractive option for both beginners and experienced developers. Whether you're building a simple website or a complex application, Django provides the tools you need to get the job done efficiently."
    }
]

post_using_id = [
    {
        'id':1,
        'title': "introduction",
        'content':"Django is a high-level web framework designed for rapid development and clean, pragmatic design. It was created by experienced developers and takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel."
    },
    {
        'id': 2,
        'title': "Key Features of Django",
        'content':""
    },
    {
        'id': 3,
        'title': "Model-View-Template (MVT) Architecture",
        'content':"Django follows the MVT architecture pattern, which is similar to the MVC (Model-View-Controller) pattern. This separates the data model, business logic, and user interface, making the codebase easier to manage."
    },
    {
        'id': 4,
        'title': "ORM (Object-Relational Mapping)",
        'content':"Django includes a powerful ORM that allows you to interact with your database using Python code instead of writing SQL queries. This makes it easier to work with databases."
    },
    {
        'id': 5,
        'title': "Admin Interface",
        'content':"Django automatically generates an admin interface for your models, allowing you to manage your application’s data through a web-based interface without writing any additional code."
    },
    {
        'id': 6,
        'title': "Security",
        'content':"Django provides built-in protections against many common security threats, such as SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking."
    },
    {
        'id': 7,
        'title': "Scalability",
        'content':"Django is designed to handle high traffic and can be scaled to meet the needs of large, complex web applications. It’s used by many high-traffic sites like Instagram and Pinterest."
    },
    {
        'id': 8,
        'title': "Batteries-Included",
        'content':"Django comes with a wide array of built-in features and utilities, from authentication and session management to URL routing and template rendering. This reduces the need for external libraries."
    },
    {
        'id': 9,
        'title': "Community and Documentation",
        'content':"Django has a large and active community, and its documentation is among the best for any open-source project. This makes it easy to find help, tutorials, and third-party packages."
    },
    {
        'id': 10,
        'title': "Getting Started with Django",
        'content':"""To get started with Django, follow these steps:

Install Django: You can install Django using pip:
sh
pip install django

Create a New Project: Start a new Django project with the following command:
sh
django-admin startproject myproject

Create an App: Inside your project, create an app with the following command:
sh
python manage.py startapp myapp

Run the Development Server: Start the development server to see your project in action:
sh
python manage.py runserver

Start Building: Now you can start building your models, views, and templates."""
    },
    {
        'id': 0,
        'title': "",
        'content':""
    },
]

def home_1(request):
    htmlPage = ''
    for article in power_of_django:
        for topics, content in article.items():
            if isinstance(content,dict):
                for topic, point  in content.items():
                    topic = topic.replace('_', " ")
                    htmlPage += f"""
                        <div>
                            <ul>
                                <li>
                                    <h2>{topic.upper()}: </h2>
                                    <p>{point}</p>
                                </li>
                            <ul>
                        </div>
                    """
            else:
                topics = topics.replace("_", " ")
                htmlPage += f"""
                <div>
                    <h1>{topics.upper()}</h1>
                    <p>{content}</p>
                </div>
                """
            
    return HttpResponse(htmlPage)

def home(request):
    html_page = ""
    for topic in post_using_id:
        html_page += f"""
        <div>
            <a href='/post/{topic['id']}/'>
                <h1>{topic['title'].title()}</h1>
            </a>
            <p>{topic['content']}</p>
        </div>
        """
    return HttpResponse(html_page)

def post(request, id):
    is_valid = False
    for post in post_using_id:
        if post['id'] == id:
            post_dict = post
            is_valid = True
            break
    if is_valid:
        html_page = f"""
        <h1>{post_dict['title'].upper()}</h1>
        <p>{post_dict['content']}</p>
        """
        return HttpResponse(html_page)
    else:
        return HttpResponseNotFound("Page not found :-(")