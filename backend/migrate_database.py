"""
Migration script to add Conversation and Message tables to the database.

This script adds the new tables required for the Phase III Todo AI Chatbot
without modifying existing tables or data.
"""

import os
from sqlalchemy import create_engine, text
from settings import settings

def migrate_database():
    """Apply the database migration to add Conversation and Message tables."""
    # Create database engine
    engine = create_engine(settings.database_url)
    
    # SQL statements to create the new tables
    create_conversations_table = """
    CREATE TABLE IF NOT EXISTS conversations (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    create_messages_table = """
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        conversation_id INTEGER NOT NULL,
        role VARCHAR(20) NOT NULL CHECK (role IN ('user', 'assistant')),
        content TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES conversations(id)
    );
    """
    
    create_indexes = """
    CREATE INDEX IF NOT EXISTS idx_messages_conversation_id ON messages(conversation_id);
    CREATE INDEX IF NOT EXISTS idx_messages_user_id ON messages(user_id);
    CREATE INDEX IF NOT EXISTS idx_conversations_user_id ON conversations(user_id);
    """
    
    # Execute the migration
    with engine.connect() as conn:
        # Execute each statement
        conn.execute(text(create_conversations_table))
        conn.execute(text(create_messages_table))
        conn.execute(text(create_indexes))
        
        # Commit the transaction
        conn.commit()
    
    print("Database migration completed successfully!")
    print("- Created conversations table")
    print("- Created messages table") 
    print("- Created indexes for performance")
    print("- Maintained all existing data and tables")


if __name__ == "__main__":
    migrate_database()