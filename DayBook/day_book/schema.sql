CREATE TABLE IF NOT EXISTS day_book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    performance TEXT NOT NULL DEFAULT '1/0',
    place TEXT DEFAULT 'Home',
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
