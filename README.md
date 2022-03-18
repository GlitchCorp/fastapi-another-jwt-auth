<h1 align="left" style="margin-bottom: 20px; font-weight: 500; font-size: 50px; color: black;">
  FastAPI Another JWT Auth
</h1>

![Tests](https://github.com/GlitchCorp/fastapi-another-jwt-auth/workflows/Tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/GlitchCorp/fastapi-another-jwt-auth/badge.svg?branch=master)](https://coveralls.io/github/GlitchCorp/fastapi-another-jwt-auth?branch=master)
[![PyPI version](https://badge.fury.io/py/fastapi-another-jwt-auth.svg)](https://badge.fury.io/py/fastapi-another-jwt-auth)
[![Downloads](https://static.pepy.tech/personalized-badge/fastapi-another-jwt-auth?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/fastapi-another-jwt-auth)

---

**Documentation**: <a href="https://GlitchCorp.github.io/fastapi-another-jwt-auth" target="_blank">https://GlitchCorp.github.io/fastapi-another-jwt-auth</a>

**Source Code**: <a href="https://github.com/GlitchCorp/fastapi-another-jwt-auth" target="_blank">https://github.com/GlitchCorp/fastapi-another-jwt-auth</a>

---

## Features
FastAPI extension that provides JWT Auth support (secure, easy to use and lightweight), if you were familiar with flask-jwt-extended this extension suitable for you, cause this extension inspired by flask-jwt-extended 😀

- Access tokens and refresh tokens
- Freshness Tokens
- Revoking Tokens
- Support for WebSocket authorization
- Support for adding custom claims to JSON Web Tokens
- Storing tokens in cookies and CSRF protection

## Installation
The easiest way to start working with this extension with pip

```bash
pip install fastapi-another-jwt-auth
```

If you want to use asymmetric (public/private) key signing algorithms, include the <b>asymmetric</b> extra requirements.
```bash
pip install 'fastapi-another-jwt-auth[asymmetric]'
```

## License
This project is licensed under the terms of the MIT license.
