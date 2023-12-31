PGDMP  4                
    {            service_board_db    16.0    16.0 $               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16783    service_board_db    DATABASE     �   CREATE DATABASE service_board_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
     DROP DATABASE service_board_db;
                postgres    false            �            1259    16811 	   tb_jobest    TABLE     �   CREATE TABLE public.tb_jobest (
    id smallint NOT NULL,
    jobreq_no smallint NOT NULL,
    transact_date date NOT NULL,
    sticker_no character varying(7)
);
    DROP TABLE public.tb_jobest;
       public         heap    postgres    false            �            1259    16810    tb_jobest_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_jobest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.tb_jobest_id_seq;
       public          postgres    false    218                       0    0    tb_jobest_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.tb_jobest_id_seq OWNED BY public.tb_jobest.id;
          public          postgres    false    217            �            1259    16785 	   tb_jobreq    TABLE     +  CREATE TABLE public.tb_jobreq (
    user_id smallint NOT NULL,
    jobreq_no smallint NOT NULL,
    jobreq_date date NOT NULL,
    jobreq_stat smallint NOT NULL,
    jobcont smallint NOT NULL,
    plate_no character varying(7),
    sticker_no character varying(6) NOT NULL,
    appoint smallint NOT NULL,
    CONSTRAINT tb_jobreq_appoint_check CHECK ((appoint = ANY (ARRAY[1, 2, 3, 4]))),
    CONSTRAINT tb_jobreq_jobcont_check CHECK ((jobcont = ANY (ARRAY[0, 1]))),
    CONSTRAINT tb_jobreq_jobreq_stat_check CHECK ((jobreq_stat = ANY (ARRAY[0, 1])))
);
    DROP TABLE public.tb_jobreq;
       public         heap    postgres    false            �            1259    16838    tb_jobreq_technician    TABLE     �   CREATE TABLE public.tb_jobreq_technician (
    id smallint NOT NULL,
    user_id smallint NOT NULL,
    "time" timestamp without time zone NOT NULL
);
 (   DROP TABLE public.tb_jobreq_technician;
       public         heap    postgres    false            �            1259    16837    tb_jobreq_technician_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_jobreq_technician_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.tb_jobreq_technician_id_seq;
       public          postgres    false    220                       0    0    tb_jobreq_technician_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.tb_jobreq_technician_id_seq OWNED BY public.tb_jobreq_technician.id;
          public          postgres    false    219            �            1259    16784    tb_jobreq_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_jobreq_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.tb_jobreq_user_id_seq;
       public          postgres    false    216                       0    0    tb_jobreq_user_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.tb_jobreq_user_id_seq OWNED BY public.tb_jobreq.user_id;
          public          postgres    false    215            �            1259    16857 	   tb_repair    TABLE     }   CREATE TABLE public.tb_repair (
    id integer NOT NULL,
    jobreq_no smallint NOT NULL,
    repair_no smallint NOT NULL
);
    DROP TABLE public.tb_repair;
       public         heap    postgres    false            �            1259    16856    tb_repair_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_repair_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.tb_repair_id_seq;
       public          postgres    false    222                       0    0    tb_repair_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.tb_repair_id_seq OWNED BY public.tb_repair.id;
          public          postgres    false    221            `           2604    16830    tb_jobest id    DEFAULT     l   ALTER TABLE ONLY public.tb_jobest ALTER COLUMN id SET DEFAULT nextval('public.tb_jobest_id_seq'::regclass);
 ;   ALTER TABLE public.tb_jobest ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            _           2604    16822    tb_jobreq user_id    DEFAULT     v   ALTER TABLE ONLY public.tb_jobreq ALTER COLUMN user_id SET DEFAULT nextval('public.tb_jobreq_user_id_seq'::regclass);
 @   ALTER TABLE public.tb_jobreq ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    216    215    216            a           2604    16849    tb_jobreq_technician id    DEFAULT     �   ALTER TABLE ONLY public.tb_jobreq_technician ALTER COLUMN id SET DEFAULT nextval('public.tb_jobreq_technician_id_seq'::regclass);
 F   ALTER TABLE public.tb_jobreq_technician ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            b           2604    16860    tb_repair id    DEFAULT     l   ALTER TABLE ONLY public.tb_repair ALTER COLUMN id SET DEFAULT nextval('public.tb_repair_id_seq'::regclass);
 ;   ALTER TABLE public.tb_repair ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222                      0    16811 	   tb_jobest 
   TABLE DATA           M   COPY public.tb_jobest (id, jobreq_no, transact_date, sticker_no) FROM stdin;
    public          postgres    false    218   m*                 0    16785 	   tb_jobreq 
   TABLE DATA           y   COPY public.tb_jobreq (user_id, jobreq_no, jobreq_date, jobreq_stat, jobcont, plate_no, sticker_no, appoint) FROM stdin;
    public          postgres    false    216   �*                 0    16838    tb_jobreq_technician 
   TABLE DATA           C   COPY public.tb_jobreq_technician (id, user_id, "time") FROM stdin;
    public          postgres    false    220   �+       	          0    16857 	   tb_repair 
   TABLE DATA           =   COPY public.tb_repair (id, jobreq_no, repair_no) FROM stdin;
    public          postgres    false    222   	,                  0    0    tb_jobest_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.tb_jobest_id_seq', 1, false);
          public          postgres    false    217                       0    0    tb_jobreq_technician_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.tb_jobreq_technician_id_seq', 1, false);
          public          postgres    false    219                       0    0    tb_jobreq_user_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.tb_jobreq_user_id_seq', 1, false);
          public          postgres    false    215                       0    0    tb_repair_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.tb_repair_id_seq', 1, false);
          public          postgres    false    221            k           2606    16832    tb_jobest tb_jobest_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.tb_jobest
    ADD CONSTRAINT tb_jobest_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.tb_jobest DROP CONSTRAINT tb_jobest_pkey;
       public            postgres    false    218            g           2606    16824    tb_jobreq tb_jobreq_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.tb_jobreq
    ADD CONSTRAINT tb_jobreq_pkey PRIMARY KEY (user_id);
 B   ALTER TABLE ONLY public.tb_jobreq DROP CONSTRAINT tb_jobreq_pkey;
       public            postgres    false    216            m           2606    16851 .   tb_jobreq_technician tb_jobreq_technician_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.tb_jobreq_technician
    ADD CONSTRAINT tb_jobreq_technician_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.tb_jobreq_technician DROP CONSTRAINT tb_jobreq_technician_pkey;
       public            postgres    false    220            o           2606    16862    tb_repair tb_repair_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.tb_repair
    ADD CONSTRAINT tb_repair_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.tb_repair DROP CONSTRAINT tb_repair_pkey;
       public            postgres    false    222            i           2606    16809    tb_jobreq unique_jobreq_no 
   CONSTRAINT     Z   ALTER TABLE ONLY public.tb_jobreq
    ADD CONSTRAINT unique_jobreq_no UNIQUE (jobreq_no);
 D   ALTER TABLE ONLY public.tb_jobreq DROP CONSTRAINT unique_jobreq_no;
       public            postgres    false    216            p           2606    16817 "   tb_jobest tb_jobest_jobreq_no_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_jobest
    ADD CONSTRAINT tb_jobest_jobreq_no_fkey FOREIGN KEY (jobreq_no) REFERENCES public.tb_jobreq(jobreq_no);
 L   ALTER TABLE ONLY public.tb_jobest DROP CONSTRAINT tb_jobest_jobreq_no_fkey;
       public          postgres    false    216    218    4713            q           2606    16844 6   tb_jobreq_technician tb_jobreq_technician_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_jobreq_technician
    ADD CONSTRAINT tb_jobreq_technician_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.tb_jobreq(user_id);
 `   ALTER TABLE ONLY public.tb_jobreq_technician DROP CONSTRAINT tb_jobreq_technician_user_id_fkey;
       public          postgres    false    220    216    4711            r           2606    16863 "   tb_repair tb_repair_jobreq_no_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_repair
    ADD CONSTRAINT tb_repair_jobreq_no_fkey FOREIGN KEY (jobreq_no) REFERENCES public.tb_jobreq(jobreq_no);
 L   ALTER TABLE ONLY public.tb_repair DROP CONSTRAINT tb_repair_jobreq_no_fkey;
       public          postgres    false    216    4713    222               a   x�E�9�0њ�.
Hje�H�x�}�sXl�vFI�)k+}�Cd@��`ш�_�e�.He@��J�T{A#Ms�١����n�? PNL         �   x�E�I�0е}�B��Yv�@� q�s`��Q�d���d c2Xc]E��īi;��Cׇ�j ��Յ0�n˚�l�d��%a�0�l96p�r^`��BH�0N|���S0;㊴%��ِ�^�/$i�����Ӭ��0WX�;���h��B���mR��_�0*��Ӽ=m�3v��{@�*6;I         Y   x�M���0�w\� ��qH���^��j���y �G	KA���s:����z[��T�@���1��q�X��\���w�������      	   !   x�3�440�\F �Lp�(����� ��7     