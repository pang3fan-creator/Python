from django_redis import get_redis_connection

redis_conn = get_redis_connection(alias='default')

redis_conn.set("abcdef", "123456")
