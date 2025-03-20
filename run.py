import os
import uvicorn
from dotenv import load_dotenv
from mangum import Mangum

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", "8001"))
    debug = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    
    # Run the application
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=debug
    )