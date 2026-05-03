from sqlalchemy.orm import Session
from database import engine, SessionLocal  # Your database setup
from models import Base, EyeColor

# Create tables
Base.metadata.create_all(bind=engine)

# Populate eye_colors
def init_eye_colors():
    db = SessionLocal()
    try:
        # Check if already populated
        if db.query(EyeColor).count() > 0:
            print("Eye colors already exist, skipping...")
            return
        
        eye_colors = [
            EyeColor(color="blue"),
            EyeColor(color="brown"),
            EyeColor(color="green"),
            EyeColor(color="hazel"),
            EyeColor(color="yellow"),
            EyeColor(color="red"),
            EyeColor(color="black"),
            EyeColor(color="orange"),
            EyeColor(color="purple"),
        ]
        
        db.add_all(eye_colors)
        db.commit()
        print(f"Added {len(eye_colors)} eye colors!")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_eye_colors()
    
    