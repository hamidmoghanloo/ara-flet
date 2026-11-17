# AdminPanel — Login / Register / Dashboard (PySide6)

A pure-Python desktop app: animated blue/black login & register screens
(with a real captcha), backed by PostgreSQL, leading into an admin dashboard
that lists every registered user.

## Run it in PyCharm

1. Unzip `AdminPanelApp.zip` and open the `AdminPanelApp` folder as a
   PyCharm project.
2. In PyCharm: **File → Settings → Project → Python Interpreter →
   Add Interpreter** (or just use the terminal at the bottom).
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. The local PostgreSQL defaults are `localhost:5432`, database `ara_flet`,
   user `postgres`, and password `12345` (the password can be overridden with
   `PGPASSWORD` if your local PostgreSQL uses a different one):
   ```powershell
   $env:PGHOST = "localhost"
   $env:PGPORT = "5432"
   $env:PGDATABASE = "ara_flet"
   $env:PGUSER = "postgres"
   $env:PGPASSWORD = "your-postgres-password"
   ```
   `pgAdmin` is a database management interface; the app connects to the
   PostgreSQL server that pgAdmin manages.
5. To copy existing accounts from `users.db` into PostgreSQL, run once:
   ```powershell
   python migrate_sqlite_to_postgres.py
   ```
   The migration keeps user IDs and timestamps. Existing IDs are skipped,
   and conflicting emails stop the transaction. Keep `users.db` as a backup
   until you confirm the migration.
6. Right-click `main.py` → **Run 'main'**. A 1280×820 desktop window opens.

No other language, framework, or build tool is involved — everything is
plain Python + PySide6 (Qt for Python), run straight from PyCharm.

## What's inside

| File | Purpose |
|---|---|
| `main.py` | App entry point, switches between Login / Register / Dashboard |
| `login_page.py` | Login screen (email + password, animated background) |
| `register_page.py` | Registration screen: name, age, email, password, confirm, **captcha** |
| `captcha.py` | Generates a random 5-character code and draws a distorted image of it (noise lines/dots, rotated letters) — no third-party image library needed |
| `dashboard_page.py` | Sidebar + header + central data table + footer, listing every registered user |
| `animated_background.py` | Floating glowing particles painted on a QTimer — the "motion in background" |
| `db.py` | PostgreSQL storage (table created automatically on first run) |
| `migrate_sqlite_to_postgres.py` | One-time import of existing `users.db` accounts |
| `style.qss` | The blue-and-black theme applied to every screen |

## How it works

- **Register**: fill the form, solve the captcha shown in the image
  (click the ⟲ icon for a new code if it's hard to read), submit. The
  user is saved to PostgreSQL's `users` table.
- **Login**: enter the email/password you registered with.
- **Dashboard**: shows every registered user's **name, age, email, and
  password** in a sortable/searchable table, plus a live count in the
  header. Use the search box to filter by name or email, and "Refresh"
  to reload after a new registration.
- **Log Out** (bottom of the sidebar) returns you to the login screen.

## A note on the passwords column

The dashboard intentionally displays raw passwords in the table, as
requested. For any real-world / production app, passwords should be
hashed (e.g. with `bcrypt`) before storage and never displayed in
plain text — happy to wire that in if you'd like a more secure version.
