import save_img_to_db as img_db

if __name__ == "__main__":
    img_db.create_image_db()
    img_db.insert_random_image()