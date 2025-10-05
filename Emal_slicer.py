# 📧 Email Slicer

def email_slicer(email):
    try:
        username, domain = email.split('@')
        domain_name = domain.split('.')[0]
        return username, domain_name
    except ValueError:
        print("❌ Invalid email format! Please include '@' in your email.")
        return None, None


def main():
    print("📧 Welcome to Email Slicer 📧")

    while True:
        email = input("\nEnter your email address (or type 'exit' to quit): ").strip()
        if email.lower() == "exit":
            print("👋 Exiting... Goodbye!")
            break

        username, domain = email_slicer(email)

        if username and domain:
            print(f"👤 Username: {username}")
            print(f"🌐 Domain: {domain}")


if __name__ == "__main__":
    main()
