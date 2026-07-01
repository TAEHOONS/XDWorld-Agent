"""
DB 마이그레이션: user_id 컬럼 추가
"""
from sqlalchemy import text
from app.db.database import engine

def migrate():
    with engine.connect() as conn:
        # conversations 테이블에 user_id 추가
        conn.execute(text("""
            ALTER TABLE conversations 
            ADD COLUMN IF NOT EXISTS user_id VARCHAR(255) NOT NULL DEFAULT 'anonymous'
        """))
        
        # user_id 인덱스 추가
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_conversations_user_id 
            ON conversations(user_id)
        """))
        
        # message_embeddings에 user_id 인덱스 추가 (JOIN 최적화)
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_message_embeddings_user_id 
            ON message_embeddings(message_id)
        """))
        
        conn.commit()
        print("✅ 마이그레이션 완료")

if __name__ == "__main__":
    migrate()
