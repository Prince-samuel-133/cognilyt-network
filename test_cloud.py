import os
try:
    from supabase import create_client
    print("✅ Supabase Library is INSTALLED!")
except ImportError:
    print("❌ Library not found. Run: python -m pip install supabase")
    
  