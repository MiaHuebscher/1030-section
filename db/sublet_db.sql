# Create and use the Sublet database
create database Sublet;
use Sublet;

# Create the tables of the database
create table sublessors (
    sbless_id integer unique not null,
    sbless_user varchar(50) unique not null,
    sbless_gender varchar(15) not null,
    sbless_age integer not null,
    primary key (sbless_id)
);

create table subletters (
    sublett_id integer unique not null,
    sblett_user varchar(50) unique not null,
    sblett_age integer not null,
    sblett_gender varchar(15) not null,
    primary key (sublett_id)
);

create table employees (
    emp_end_date date,
    emp_start_date date not null,
    emp_id integer auto_increment not null,
    work_email varchar(50) not null,
    primary key (emp_id)
);

create table posts (
    post_id integer auto_increment not null,
    sbless_id integer not null,
    post_dscrptn longtext not null,
    unit_price decimal(19,2) not null,
    emp_id integer,
    street varchar(50) not null,
    city varchar(50) not null,
    zip_code varchar(15),
    move_in date not null,
    move_out date not null,
    primary key (post_id),
    constraint sbless_fk
        foreign key (sbless_id) references sublessors (sbless_id)
        on update cascade
        on delete cascade,
    constraint emp_fk
        foreign key (emp_id) references employees (emp_id)
        on update restrict
        on delete set null
);

create table roommates (
    roommate_gender varchar(15) not null,
    roommate_id integer auto_increment not null,
    post_id integer not null,
    roommate_name varchar(100) not null,
    roommate_age integer not null,
    primary key (roommate_id),
    constraint posts_fk
        foreign key (post_id) references posts (post_id)
        on update restrict
        on delete cascade
);

create table messages (
    message_id integer auto_increment not null,
    post_id integer,
    sblett_user varchar(50) not null,
    sbless_user varchar(50) not null,
    content longtext not null,
    primary key (message_id),
    constraint sblett_user_fk
        foreign key (sblett_user) references subletters (sblett_user)
        on update cascade
        on delete cascade,
    constraint sbless_user_fk
        foreign key (sbless_user) references sublessors (sbless_user)
        on update cascade
        on delete cascade,
    constraint mess_posts_fk
        foreign key (post_id) references posts (post_id)
        on update restrict
        on delete set null
);

create table reviews (
    review_id integer auto_increment not null,
    rev_content longtext not null,
    sblett_user varchar(50) not null,
    sbless_user varchar(50) not null,
    rating integer not null,
    primary key (review_id),
    constraint rev_sblett_fk
        foreign key (sblett_user) references subletters (sblett_user)
        on update cascade
        on delete cascade,
    constraint rev_sbless_fk
        foreign key (sbless_user) references sublessors (sbless_user)
        on update cascade
        on delete cascade
);

create table landlords (
    lord_id integer auto_increment not null,
    lord_phone varchar(25) not null,
    lord_name varchar(100) not null,
    primary key (lord_id)
);

create table leases (
    lease_id integer auto_increment not null,
    sbless_id integer not null,
    rent decimal(19,2) not null,
    lease_start_date date not null,
    lease_end_date date not null,
    lord_id integer unique,
    primary key (lease_id),
    constraint lease_sbless_fk
        foreign key (sbless_id) references sublessors (sbless_id)
        on update cascade
        on delete cascade,
    constraint lease_lord_fk
        foreign key (lord_id) references landlords (lord_id)
        on update restrict
        on delete set null
);

create table photos (
    image_id integer auto_increment not null,
    image blob,
    photo_dscrptn mediumtext not null,
    post_id integer not null,
    primary key (image_id),
    constraint photos_posts_fk
        foreign key (post_id) references posts (post_id)
        on update restrict
        on delete cascade
);

create table apartment_units (
    apartment_id integer auto_increment not null,
    kitchen boolean not null,
    living_room boolean not null,
    num_bedroom integer not null,
    num_bathroom integer not null,
    post_id integer unique not null,
    primary key (apartment_id),
    constraint apart_posts_fk
        foreign key (post_id) references posts (post_id)
        on update restrict
        on delete cascade
);

create table amenities (
    apartment_id integer unique not null,
    parking boolean not null,
    rec_center boolean not null,
    mail_room boolean not null,
    guard boolean not null,
    laundry boolean not null,
    wifi boolean not null,
    electricity boolean not null,
    hot_water boolean not null,
    primary key (apartment_id),
    constraint amen_apart_fk
        foreign key (apartment_id) references apartment_units (apartment_id)
        on update restrict
        on delete cascade
);

-- Insertions
# Insert 2 rows of values into the sublessors table
insert into sublessors (sbless_id, sbless_user, sbless_age, sbless_gender)
    values (002152868, 'miahueby', 19, 'Female');
insert into sublessors (sbless_id, sbless_user, sbless_age, sbless_gender)
    values (519287789, 'jdiep', 21, 'Male');

# Insert 2 rows of values into the subletters table
insert into subletters (sublett_id, sblett_user, sblett_age, sblett_gender)
    values (129808767, 'krina_patel', 20, 'Female');
insert into subletters (sublett_id, sblett_user, sblett_age, sblett_gender)
    values (457289342, 'latkinson', 21, 'Female');

# Insert 2 rows of values into the employees table
insert into employees (emp_start_date, work_email)
    values ('2023-01-09', 'maria.gomez@sublet.com');
insert into employees (emp_start_date, work_email)
    values ('2023-01-09', 'chris.stephens@sublet.com');

# Insert 2 rows of values into the posts table
insert into posts (sbless_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out)
    values (002152868, 'Heyy, I live in a 3 bedroom apartment with two other girls who attend Northeastern Universtiy. We
            are all second-year students and love to hang out with one another and plan fun activities. Our apartment
            community (Fenway Triangle) has so many great features like a rooftop patio, a game center, a doorman,
            a fitness center, and so much more! I am going back to my hometown for the summer, so I am looking for a
            nice, respectful, and cool girl to sublet my space! The move-in date will be 5/10/2023 and the move-out date
            will be 9/07/2023. DM me for any questions!', 2500.00, 2, '180 Brookline St.', 'Boston', '02215',
            '2023-05-10', '2023-09-07');
insert into posts (sbless_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out)
    values (519287789, 'Sup!! My name is Jakob, I live with 2 other guys, and we are all juniors at Northeastern. I am
            going on co-op this fall and I am Looking to sublet my place in Mission Hill from 6/31/2023 to
            1/17/2024. You would have your own room and close access to the green and orange lines. DM me if you are
            interested', 1540.00, 1, '1518 Tremont St.', 'Boston', '02120', '2023-06-30', '2024-01-17');

# Insert 4 rows of values into the roommates table for the first two posts
insert into roommates (roommate_gender, post_id, roommate_name, roommate_age)
    values ('Female', 1, 'Lauren Thomas', 20);
insert into roommates (roommate_gender, post_id, roommate_name, roommate_age)
    values ('Female', 1, 'Casey Evans', 20);
insert into roommates (roommate_gender, post_id, roommate_name, roommate_age)
    values ('Male', 2, 'Lucas Sherman', 21);
insert into roommates (roommate_gender, post_id, roommate_name, roommate_age)
    values ('Male', 2, 'Brett Thomas', 21);

# Insert 2 rows of values into the messages table
insert into messages (post_id, sblett_user, sbless_user, content)
    values (1, 'krina_patel', 'miahueby', 'Hey girl! I am really interested in subletting your place! Maybe we can meet
            for coffee sometime this week to talk more about the process?');
insert into messages (post_id, sblett_user, sbless_user, content)
    values (2, 'latkinson', 'jdiep', 'Hey! I am desperate for a place to live this fall lol. I know you live with 2
            other boys but would they be comfortable living with a girl? I am also a third-year student at Northeastern
            and I have a boyfriend so maybe they can all be friends lol. Thanks in advance!');

# Insert 2 rows of values into the reviews table
insert into reviews (rev_content, sblett_user, sbless_user, rating)
    values ('Mia is super friendly and welcoming. She does an amazing job at answering my questions quickly and
            informatively. I would definitely recommend her as a sublessor!!', 'krina_patel', 'miahueby', 10);
insert into reviews (rev_content, sblett_user, sbless_user, rating)
    values ('Jakob is a great sublessor! He always has the information I am looking for and he responds to my messages
            quickly and respectfully. You cannot go wrong with Jakob!', 'latkinson', 'jdiep', 10);

# Insert 2 rows of values into the landlords table
insert into landlords (lord_phone, lord_name)
    values ('617-298-1067', 'Jeremy Renner');
insert into landlords (lord_phone, lord_name)
    values ('617-287-9289', 'Josh Tyler');

# Insert 2 rows of values into the leases table - before creating this information, users will have to check if their
# Landlord is already in the database by entering their name and phone number. If their landlord is in the database,
# They will enter the landlord's id number when creating their lease entry. If their landlord is not in the database,
# They will be given the option to add their landlord to the database or leave the lord_id entry null.
insert into leases (sbless_id, rent, lease_start_date, lease_end_date, lord_id)
    values (002152868, 2500.00, '2022-09-01', '2024-09-01', 1);
insert into leases (sbless_id, rent, lease_start_date, lease_end_date, lord_id)
    values (519287789, 1540.00, '2022-09-01', '2024-09-01', 2);

# Insert 2 rows of values into the photos table
insert into photos (image, photo_dscrptn, post_id)
    values (LOAD_FILE('C:\Users\19492\OneDrive - Northeastern University\Desktop\bedroom_photo.jpg'),
            'a view of my bedroom as I am standing in the doorway', 1);
insert into photos (image, photo_dscrptn, post_id)
    values (LOAD_FILE('C:\Users\19492\OneDrive - Northeastern University\Desktop\kitchen_photo'),
            'a view of the living room as I am standing in the kitchen', 2);

# Insert 2 rows of values into the apartment_units table
insert into apartment_units (kitchen, living_room, num_bedroom, num_bathroom, post_id)
    values (TRUE, TRUE, 3, 1, 1);
insert into apartment_units (kitchen, living_room, num_bedroom, num_bathroom, post_id)
    values (TRUE, TRUE, 3, 1, 2);

# Insert 2 rows of values into the amenities table
insert into amenities (apartment_id, parking, rec_center, mail_room, guard, laundry, wifi, electricity, hot_water)
    values (1, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
insert into amenities (apartment_id, parking, rec_center, mail_room, guard, laundry, wifi, electricity, hot_water)
    values (2, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE);


select post_id, sbless_user, sblett_user, content from messages
where post_id = 1 and sblett_user = 'krina_patel';