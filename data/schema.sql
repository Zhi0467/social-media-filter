-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    preferences TEXT NOT NULL
);

-- Create posts table
CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    user_id INTEGER,
    text TEXT,
    timestamp TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
