# Mesa Bite
Menu Management System

Technology Stacks:

 1. Django / Django Rest Framework (DRF)
 1. Nuxt3 (Typescript)

Why this stack? Read Here

## Local Setup Guide

### Backend (Django)
- Clone repository : `git clone https://github.com/famcodings/django_rest_reference_architecture.git`
- On main branch we are using django-rest-swagger, in order to use drf-spectacular switch to drf-spectacular-integration branch: `git checkout drf-spectacular-integration`
- Create and activate virtual environment: `pipenv shell`
- Install dependencies: `pipenv install`
- Copy .env.example in same directory and rename it as ".env" and write database and email credentials in ".env"
- Search and replace project_name with the required name of the project
- Migrate DB : `python manage.py migrate`
- Runserver : `python manage.py runserver`
- Navigate to url: `localhost:8000/swagger`

## Features
- Login API
- Logout API
- SignUp API
- Update Profile API
- Change Password API
- Reset Password APIs

## Swagger Staticfiles Error
- If you face any error in swagger related to staticfiles perform following steps to resolve it
    1. Open terminal activate virtual envirnment and run command: `pipenv --venv`.
    1. It will show the path to your virtual env directory as output. Navigate to this path.
    1. Go to: `/Lib/site-packages/rest_framework_swagger/templates/rest_framework_swagger`.
    1. Open `base.html` file in your favorite editor.
    1. Find and replace `{% load staticfiles %}` with `{% load static %}`. (Usually written at the top of the file).
    1. Save the file and restrart the server if not already running and reload the page.
- For more information related to this issue visit: `https://github.com/marcgibbons/django-rest-swagger/issues/832s`


### Frontend (Nuxt3)

# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm run build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm run preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.

---
---
----
### Why this Stack?

## Nuxt
Nuxt 3 is a Vue.js framework that provides a lot of features that are beneficial for web development. Here are some of the reasons why Nuxt 3 is a good choice for your next project:

#### 1. Improved Performance

Nuxt 3 is built on top of a new Nitro engine, which provides significant performance improvements over Nuxt 2. Nitro is a pre-rendering engine that can render your Vue.js application on the server, which can improve the initial page load time. Nitro also supports static site generation, which can make your application even faster.

#### 2. Enhanced Developer Experience

Nuxt 3 provides a number of features that can improve the developer experience, such as:

A new CLI that makes it easier to create and manage Nuxt projects
Improved tooling for code splitting and prefetching
A new API for creating custom modules
#### 3. Greater Flexibility

Nuxt 3 is more flexible than Nuxt 2, as it allows you to choose between server-side rendering (SSR), static site generation (SSG), or single-page application (SPA) mode. This flexibility allows you to choose the best rendering mode for your application's needs.

#### 4. Large Community

Nuxt has a large and active community of developers, which means that there are a lot of resources available to help you learn and use the framework. There are also a number of Nuxt modules available that can extend the functionality of your application.

#### 5. Future-Proof

Nuxt 3 is a framework that is designed to be future-proof. It is based on modern web standards and it is constantly being updated with new features. This means that you can be confident that your Nuxt application will be able to meet the needs of your users for years to come.

In addition to the benefits listed above, Nuxt 3 is also a very extensible framework. This means that you can customize it to meet the specific needs of your project.

Overall, Nuxt 3 is a powerful and flexible framework that is a good choice for a wide range of web development projects. If you are looking for a framework that can help you build high-performance, scalable, and maintainable web applications, then Nuxt 3 is a great option to consider.

#### Here are some additional benefits of using Nuxt 3:

SEO-friendly: Nuxt 3 applications are SEO-friendly, which means that they are more likely to rank high in search engine results pages (SERPs).
Accessibility: Nuxt 3 applications are accessible to users with disabilities.
Mobile-friendly: Nuxt 3 applications are mobile-friendly, which means that they will look and work great on mobile devices.
If you are considering using Nuxt 3 for your next project, I recommend that you take a look at the official Nuxt documentation. There is also a large number of community-written tutorials and articles available online.

## Django and DRF

Django and Django REST Framework (DRF) are powerful and widely used tools for backend development. They offer a combination of features that make them a great choice for a variety of projects, including:

#### 1. Rapid Development: 

Django's "batteries-included" approach provides a rich set of ready-to-use features, such as an object-relational mapper (ORM), authentication and authorization systems, and administrative interfaces. This allows developers to quickly build and deploy web applications without having to reinvent the wheel.

#### 2. Robustness and Scalability: 
Django is designed to handle high traffic and complex applications. It is built on a solid foundation of Python and provides various mechanisms for scaling, such as load balancing and caching.

#### 3. Security:
 Django incorporates various security features into its core, including protection against common vulnerabilities like SQL injection and cross-site scripting (XSS). It also supports industry-standard authentication and authorization mechanisms.

#### 4. Flexibility:
 Django's architecture allows developers to customize and extend the framework to suit specific project requirements. It integrates well with third-party libraries and tools, providing flexibility in building complex application backends.

#### 5. Django REST Framework (DRF):
 DRF is a powerful toolkit for building RESTful APIs, which are the backbone of modern web applications. It provides a clean and consistent interface for designing API endpoints, handling data serialization, and implementing authentication and authorization.

#### 6. Community and Support:
 Django and DRF enjoy large and active communities of developers, providing ample resources for learning, troubleshooting, and collaborating on projects. Extensive documentation, tutorials, and online forums are readily available.

#### 7. Maturity and Stability:
 Django and DRF have been around for many years and have undergone rigorous testing and refinement. Their maturity and stability make them reliable choices for production environments.

In summary, Django and Django REST Framework are excellent choices for backend development due to their rapid development capabilities, robustness, security, flexibility, and strong community support. They are well-suited for building a wide variety of web applications, from simple CRUD operations to complex data-driven APIs.

####  Here are some specific examples of projects where Django and DRF have been successfully used:

News websites: Django's templating system and user authentication features make it ideal for building news websites. DRF can be used to create APIs for managing articles, users, and other content.

E-commerce platforms: Django's robust ORM and support for payment gateways make it a suitable choice for e-commerce platforms. DRF can be used to create APIs for product management, shopping carts, and order processing.

Real-time applications: Django's asynchronous capabilities and integration with WebSocket frameworks enable it to handle real-time data updates and user interactions. DRF can be used to create APIs for real-time data streaming and notifications.

Data analytics dashboards: Django's ability to connect to various data sources and its rich templating system make it a good choice for building data analytics dashboards. DRF can be used to create APIs for retrieving and visualizing data.

Django and Django REST Framework are versatile tools that can empower developers to build scalable, secure, and maintainable web applications. Their popularity and extensive community support make them a valuable choice for backend development projects.



# How Nuxt3 and Django Rest Framework (DRF)  make perfect web development stack


Nuxt 3 and Django REST Framework (DRF) form a powerful web development stack that combines the strengths of both frameworks to create high-performance, scalable, and maintainable web applications. Here's how they complement each other:

#### 1. Front-end and Back-end Separation:
Nuxt 3 handles the front-end responsibilities, providing a modern Vue.js framework for building Single-Page Applications (SPAs) or Static Site Generated (SSG) websites. DRF, on the other hand, focuses on the back-end, empowering developers to create robust RESTful APIs for data management and service orchestration.

#### 2. Data Fetching and Manipulation: 
Nuxt 3's asynchronous data fetching capabilities seamlessly integrate with DRF's well-structured API endpoints. Nuxt 3's Vuex store can effectively manage and manipulate data retrieved from DRF APIs, ensuring a smooth and responsive user experience.

#### 3. Authentication and Authorization: 
DRF's built-in authentication and authorization mechanisms can be leveraged by Nuxt 3 to secure user access and protect sensitive data. Nuxt 3 can seamlessly integrate with DRF's authentication tokens, allowing users to access protected resources on the front-end.

#### 4. Real-time Communication: 
Django's support for asynchronous communication protocols, such as WebSockets, can be combined with Nuxt 3's Vuex store to implement real-time features. DRF can be used to broadcast data updates, while Nuxt 3 can handle real-time data synchronization and user interactions.

#### 5. Scalability and Performance:
 Nuxt 3's server-side rendering (SSR) and static site generation (SSG) capabilities can significantly improve page load times and initial rendering performance. DRF's efficient API design and Django's robust infrastructure ensure scalability for high-traffic applications.

#### 6. Developer Experience: 
Nuxt 3 and DRF both offer rich development environments and extensive documentation. Their large communities provide ample resources, tutorials, and support forums, making it easy for developers to learn and adopt these frameworks.

In summary, Nuxt 3 and Django REST Framework form a synergistic web development stack that addresses both front-end and back-end needs with efficiency and flexibility. Their complementary features and strong communities make them an excellent choice for building modern, performant, and secure web applications.

