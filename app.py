from flask import Flask, jsonify

app = Flask(__name__)

languages = [
    {"id": 1, "name": "Python", "creator": "Guido van Rossum", "year": 1991, "paradigm": "Object-oriented, Procedural, Functional", "description": "Python is a high-level, interpreted language known for its simplicity and readability, widely used in web development, data science, automation, and AI."},
    {"id": 2, "name": "JavaScript", "creator": "Brendan Eich", "year": 1995, "paradigm": "Event-driven, Functional, Imperative", "description": "JavaScript is a versatile scripting language primarily used for creating dynamic web pages and front-end applications."},
    {"id": 3, "name": "Java", "creator": "James Gosling", "year": 1995, "paradigm": "Object-oriented, Class-based, Concurrent", "description": "Java is a popular, platform-independent programming language used in enterprise applications, Android development, and large-scale systems."},
    {"id": 4, "name": "C++", "creator": "Bjarne Stroustrup", "year": 1985, "paradigm": "Procedural, Object-oriented, Generic", "description": "C++ is an extension of C with object-oriented features, widely used in game development, high-performance applications, and system software."},
    {"id": 5, "name": "C#", "creator": "Microsoft", "year": 2000, "paradigm": "Object-oriented, Component-oriented", "description": "C# is a modern, object-oriented language developed by Microsoft, primarily used for Windows applications, game development, and enterprise software."},
    {"id": 6, "name": "Ruby", "creator": "Yukihiro Matsumoto", "year": 1995, "paradigm": "Object-oriented, Reflective, Dynamic", "description": "Ruby is a dynamic, open-source language known for its elegant syntax and is widely used in web development with the Ruby on Rails framework."},
    {"id": 7, "name": "Swift", "creator": "Apple Inc.", "year": 2014, "paradigm": "Object-oriented, Protocol-oriented", "description": "Swift is a powerful and user-friendly programming language developed by Apple for iOS, macOS, watchOS, and tvOS applications."},
    {"id": 8, "name": "Go", "creator": "Robert Griesemer, Rob Pike, Ken Thompson", "year": 2009, "paradigm": "Compiled, Concurrent, Procedural", "description": "Go (Golang) is a statically typed, compiled language designed for high-performance, concurrent programming, developed by Google."},
    {"id": 9, "name": "HTML", "creator": "Tim Berners-Lee", "year": 1993, "paradigm": "Markup language", "description": "HTML (HyperText Markup Language) is the standard language for creating web pages and structuring content on the internet."},
    {"id": 10, "name": "CSS", "creator": "Håkon Wium Lie", "year": 1996, "paradigm": "Style sheet language", "description": "CSS (Cascading Style Sheets) is used to define the appearance and layout of web pages, allowing for responsive and visually appealing designs."},
    {"id": 11, "name": "SQL", "creator": "Donald D. Chamberlin, Raymond F. Boyce", "year": 1974, "paradigm": "Query language, Declarative", "description": "SQL (Structured Query Language) is a domain-specific language used for managing and querying relational databases."},
    {"id": 12, "name": "XML", "creator": "W3C", "year": 1996, "paradigm": "Markup language", "description": "XML (eXtensible Markup Language) is used to store and transport data in a structured, human-readable format."},
    {"id": 13, "name": "PHP", "creator": "Rasmus Lerdorf", "year": 1995, "paradigm": "Object-oriented, Procedural", "description": "PHP is a server-side scripting language primarily used for web development, powering many websites and web applications."},
    {"id": 14, "name": "TypeScript", "creator": "Microsoft", "year": 2012, "paradigm": "Object-oriented, Functional", "description": "TypeScript is a superset of JavaScript that adds static typing, enhancing scalability and maintainability of large applications."},
    {"id": 15, "name": "Kotlin", "creator": "JetBrains", "year": 2011, "paradigm": "Object-oriented, Functional", "description": "Kotlin is a modern programming language fully interoperable with Java, widely used for Android development and enterprise applications."},
    {"id": 16, "name": "R", "creator": "Ross Ihaka, Robert Gentleman", "year": 1993, "paradigm": "Statistical, Functional, Procedural", "description": "R is a programming language and environment designed for statistical computing, data visualization, and machine learning."},
    {"id": 17, "name": "Perl", "creator": "Larry Wall", "year": 1987, "paradigm": "Procedural, Functional, Object-oriented", "description": "Perl is a high-level, general-purpose scripting language known for text processing and system administration tasks."},
    {"id": 18, "name": "Lua", "creator": "Roberto Ierusalimschy", "year": 1993, "paradigm": "Procedural, Functional, Scripting", "description": "Lua is a lightweight, high-performance scripting language widely used in game development and embedded systems."},
    {"id": 19, "name": "MATLAB", "creator": "MathWorks", "year": 1984, "paradigm": "Numerical computing, Procedural", "description": "MATLAB is a powerful language for numerical computation, widely used in engineering, physics, and data analysis."},
    {"id": 20, "name": "Dart", "creator": "Google", "year": 2011, "paradigm": "Object-oriented, Functional", "description": "Dart is a client-optimized language developed by Google, mainly used for building mobile, desktop, and web applications with Flutter."},
    {"id": 21, "name": "Rust", "creator": "Mozilla", "year": 2010, "paradigm": "Functional, Concurrent, Procedural", "description": "Rust is a systems programming language focused on safety and performance, often used in web assembly, networking, and game development."},
    {"id": 22, "name": "Scala", "creator": "Martin Odersky", "year": 2003, "paradigm": "Functional, Object-oriented", "description": "Scala is a scalable language that integrates object-oriented and functional programming, mainly used in big data and distributed systems."},
    {"id": 23, "name": "COBOL", "creator": "CODASYL", "year": 1959, "paradigm": "Procedural, Object-oriented", "description": "COBOL is a legacy programming language used for business, finance, and administrative systems in governments and corporations."},
    {"id": 24, "name": "Fortran", "creator": "IBM", "year": 1957, "paradigm": "Procedural, Numeric computing", "description": "Fortran is one of the oldest programming languages, mainly used in scientific computing and engineering applications."},
    {"id": 25, "name": "Haskell", "creator": "Lennart Augustsson et al.", "year": 1990, "paradigm": "Functional, Declarative", "description": "Haskell is a purely functional programming language known for its strong type system and lazy evaluation."}
]

@app.route("/api/languages", methods=["GET"])
def get_languages():
    return jsonify(languages)

@app.route("/api/languages/<int:index>", methods=["GET"])
def get_languages_by_index(index):
    if 0 <= index < len(languages):
        return jsonify(languages[index])
    return jsonify({"error": "language not found"}), 404

@app.route("/api/languages/<string:lang_name>", methods=["GET"])
def get_languages_by_name(lang_name):
    for lang in languages:
        if lang["name"].lower() == lang_name.lower():
            return jsonify(lang)
    return jsonify({"error": "language not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)    