from dotenv import load_dotenv
import os
load_dotenv()
myvariable = os.getenv("open_ai_akey")
print(myvariable)