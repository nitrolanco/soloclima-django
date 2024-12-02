# Soloclima: A Django MongoDB Misadventure 🚨🤦‍♂️

## 🔥 Project Overview: What Were We Thinking?

Welcome to Soloclima, a prime example of how NOT to build a web application. This project is a spectacular demonstration of architectural anti-patterns, where we've taken Django - a robust web framework - and brutally misused it to create a half-baked, REST-like MongoDB interface.

### 🚨 Warning: Technical Malpractice Ahead

**Disclaimer**: This project is a cautionary tale of what happens when you ignore best practices and decide to reinvent the wheel... poorly.

## 🤔 The Questionable Concept

We've created a Django project that:

- Completely ignores Django's ORM (Because who needs robust database abstraction, right?)
- Uses MongoDB directly through `pymongo`
- Manually handles what Django would do automatically
- Breaks every convention of both Django and RESTful design

## 🛠 Technologies Abused

- **Django**: Used as a glorified template renderer
- **MongoDB**: Treated like a JSON dumping ground
- **Python**: Suffering through our terrible architectural decisions

## 💥 Why This is a Terrible Idea

### 1. Bypassing Django's ORM

- Lost automatic database migrations
- No built-in query optimization
- Manual everything = maximum developer pain

### 2. REST-Like? More Like REST-In-Peace

- No proper API framework
- Custom, inefficient data fetching
- Zero API documentation
- Completely manual routing and serialization

### 3. Performance Nightmare

- Direct MongoDB queries without caching
- No connection pooling
- Reinventing every wheel Django provides out-of-the-box

🏆 Achievement Unlocked

"Most Unnecessary Complexity in a Web Project" 🏅
"Ignoring Framework Best Practices" 🚩
"Maximum Effort, Minimum Efficiency" 🏆

📦 Installation (If You Dare)
bashCopy# Clone this monument to poor decisions
git clone https://github.com/your-username/soloclima.git

# Install dependencies (hope you like troubleshooting)

pip install -r requirements.txt

# Run the server and question your life choices

python manage.py runserver
