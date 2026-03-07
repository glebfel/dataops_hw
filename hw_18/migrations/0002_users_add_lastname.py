from yoyo import step

__depends__ = {"0001_users_create_table"}

steps = [
    step(
        """
        ALTER TABLE users
        ADD COLUMN IF NOT EXISTS lastname VARCHAR(255);
        """,
        """
        ALTER TABLE users
        DROP COLUMN IF EXISTS lastname;
        """
    )
]
