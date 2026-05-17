from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)


@app.route('/user')
def get_user():
    # SQL Injection — intentionally vulnerable for scanner test
    # Detected by: Semgrep default p/python ruleset (tainted-sql-string)
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return str(cursor.fetchall())


@app.route('/go')
def unsafe_redirect():
    # Open Redirect — redirect destination taken directly from request
    # parameter without validation. An attacker can redirect users to
    # a malicious external site after visiting a trusted URL.
    # Detected by: Semgrep custom flask-open-redirect rule (CWE-601)
    url = request.args.get('url')
    return redirect(url)


if __name__ == '__main__':
    # Security Misconfiguration — debug mode enabled.
    # Activates the Werkzeug interactive debugger which allows
    # arbitrary code execution via the browser on any exception.
    # Detected by: Semgrep custom flask-debug-mode rule (CWE-94)
    app.run(debug=True)