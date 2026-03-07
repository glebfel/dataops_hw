from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
        """,
        """
        DROP TABLE IF EXISTS users;
        """
    )
]
