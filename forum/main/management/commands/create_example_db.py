from random import randint

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

from main.models import BigGroup, Group, Topic, Post

from users.models import UtcOffset


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_utcoffsets()
        self.create_users()
        self.create_biggroups_and_groups()
        self.create_topics()
        self.create_posts()
        self.create_superuser()
        return "Example data base is done!"

    def create_utcoffsets(self):
        UtcOffset.objects.all().delete()
        for index in range(0, 9):
            UtcOffset.objects.create(
                description=f"MSK+{index}",
                offset=index + 3,
            )

    def create_users(self):
        get_user_model().objects.all().delete()
        usernames = ["Вова", "Оля", "Миша", "Наташа", "Борис", "Света", "Леон", "Лулу", "Светозар"]
        index = 1
        while True:
            try:
                with open(f"example_db_data/users_avatars/{index}.jpg", "rb") as f:
                    image_bytes = f.read()
            except FileNotFoundError:
                break
            get_user_model().objects.create_user(
                username=usernames[index % (len(usernames) - 1)],
                # username=f"user{index}",
                password=usernames[index % (len(usernames) - 1)],
                image=SimpleUploadedFile("example_user_avatar.jpg", image_bytes),
                utc_offset=UtcOffset.objects.first(),
            )
            index += 1
        return "Users created!\n"

    def create_biggroups_and_groups(self):
        BigGroup.objects.all().delete()
        Group.objects.all().delete()
        index = 0
        while True:
            try:
                with open(f"example_db_data/biggroups{index}.txt", encoding="utf8") as f:
                    names = f.readlines()
            except FileNotFoundError:
                break
            big_group = BigGroup.objects.create(name=names[0])
            del names[0]
            Group.objects.bulk_create(Group(name=name, big_group=big_group) for name in names)
            index += 1
        return "Biggroups and Groups created!\n"

    def create_topics(self):
        Topic.objects.all().delete()
        with open("example_db_data/topics.txt", encoding="utf8") as f:
            topic_names = f.readlines()
        with open("example_db_data/smiles.txt", encoding="utf8") as f:
            smiles = f.readline()
        groups = Group.objects.all()
        i = 0
        for group in groups:
            topics_num = randint(int(settings.TOPICS_LIMIT_IN_GROUP / 3), settings.TOPICS_LIMIT_IN_GROUP)
            for _ in range(topics_num):
                users = list(get_user_model().objects.all())
                rand_user = users[randint(0, len(users) - 1)]
                rand_name = topic_names[randint(1, len(topic_names) - 1)]
                smile_index = randint(1, len(smiles))
                rand_smile = smiles[smile_index] if (smile_index % 3 == 0) else ""
                rand_views_count = randint(int(settings.POSTS_LIMIT_IN_TOPIC * 2), settings.POSTS_LIMIT_IN_TOPIC * 5)
                Topic.objects.create(
                    group=group,
                    author=rand_user,
                    name=rand_name+rand_smile,
                    views_count=rand_views_count,
                )
                i += 1
                print(f"topic {i} created")
        return "All topics created!\n"

    def create_posts(self):
        Post.objects.all().delete()
        with open("example_db_data/posts.txt", encoding="utf8") as f:
            post_contents = f.readlines()
        with open("example_db_data/smiles.txt", encoding="utf8") as f:
            smiles = f.readline()

        image_files = {}
        image_index = 0
        while True:
            try:
                with open(f"example_db_data/post_images/image{image_index}.png", "rb") as f:
                    image_bytes = f.read()
            except FileNotFoundError:
                break
            image_files[image_index] = SimpleUploadedFile("example_picture.png", image_bytes)
            image_index += 1

        topics = Topic.objects.all()
        i = 0
        for topic in topics:
            posts_num = randint(int(settings.POSTS_LIMIT_IN_TOPIC / 3), settings.POSTS_LIMIT_IN_TOPIC)
            for _ in range(posts_num):
                users = list(get_user_model().objects.all())
                rand_user = users[randint(0, len(users) - 1)]
                rand_content = post_contents[randint(1, len(post_contents) - 1)]
                smile_index = randint(1, len(smiles))
                rand_smile = smiles[smile_index] if (smile_index % 3 == 0) else ""
                new_post = Post.objects.create(
                    topic=topic,
                    author=rand_user,
                    content=rand_content+rand_smile,
                )
                if randint(1, 5) == 1:  # вставляем картинки с вероятностью 1/5
                    image_index = randint(0, len(image_files) - 1)
                    new_post.image = image_files[image_index]
                    new_post.save()
                i += 1
                print(f"Post {i} created")
        return "All posts created!\n"

    def create_superuser(self):
        get_user_model().objects.create_user(
            username="admin",
            password="admin",
            is_staff=True,
            utc_offset=UtcOffset.objects.first(),
            )
        return "Superusercreated!\n"
