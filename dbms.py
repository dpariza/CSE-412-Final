import psycopg2
import psycopg2.extras
import pandas as pd

db_name = 'la_airbnb_412'
db_user = 'postgres'
db_password = '1301'
db_host = 'localhost'
port_id = '5432'


def execute_query(min_price, max_price, bedrooms, accommodates, neighborhood, checkin_date, checkout_date):
    try:
        conn = psycopg2.connect(dbname=db_name,
                                user=db_user,
                                password=db_password,
                                host=db_host,
                                port=port_id)

        cur = conn.cursor()

        if checkin_date is not None and checkout_date is not None:
            date_range = pd.date_range(start=checkin_date, end=checkout_date).strftime('%Y-%m-%d').tolist()
            date_count = len(date_range)
            date_range_string = ""
            for date in date_range:
                date_range_string += f"'{date}', "
            date_range_string = date_range_string[:-2]

            query_select = f'''
            WITH VALID_LISTINGS AS
                (SELECT COUNT(AVAILABLE), LISTING_ID FROM
                    (SELECT listing_id, date, available
                    FROM CALENDAR
                    WHERE DATE IN ({date_range_string})
                    AND AVAILABLE IS TRUE
                    ) AS AVAIL_CHECK
                GROUP BY LISTING_ID
                HAVING COUNT(AVAILABLE) = {date_count}
                )
            SELECT  L.picture_url AS Picture,
                    L.name AS Name,
                    L.description AS Neighborhood, --these are swapped oops
                    L.neighborhood AS Description,
                    BI.price AS Price,
                    LI.bedrooms AS Bedrooms,
                    LI.accommodates AS accommodates,
                    RS.review_scores_rating AS Rating
            FROM VALID_LISTINGS AS VL
            NATURAL JOIN LISTINGS AS L
            NATURAL JOIN LISTING_INFO AS LI
            NATURAL JOIN BOOKING_INFO AS BI
            NATURAL JOIN REVIEW_STATS AS RS
            '''
        else:
            query_select = f'''
            SELECT  L.picture_url AS Picture,
                    L.name AS Name,
                    L.description AS Neighborhood, --these are swapped oops
                    L.neighborhood AS Description,
                    BI.price AS Price,
                    LI.bedrooms AS Bedrooms,
                    LI.accommodates AS accommodates,
                    RS.review_scores_rating AS Rating
            FROM LISTINGS AS L
            NATURAL JOIN LISTING_INFO AS LI
            NATURAL JOIN BOOKING_INFO AS BI
            NATURAL JOIN REVIEW_STATS AS RS
            '''

        query_where = '''WHERE TRUE
        '''

        if min_price is not None:
            query_where += f''' AND BI.price >= {min_price}
            '''

        if max_price is not None:
            query_where += f'''AND BI.price <= {max_price}
            '''

        if bedrooms is not None:
            query_where += f'''AND LI.bedrooms = {bedrooms}
            '''

        if accommodates is not None:
            query_where += f'''AND LI.accommodates = {accommodates}
            '''

        if neighborhood != "All Neighborhoods" and neighborhood is not None:
            query_where += f'''AND L.description = '{neighborhood}' --these are swapped in the dbms by mistake
            '''

        query_where += '''AND RS.review_scores_rating IS NOT NULL
			ORDER BY RS.review_scores_rating desc'''

        query = query_select + query_where

        cur.execute(query)

        df = pd.DataFrame(cur.fetchall(),
                          columns=['Picture', 'Name', 'Neighborhood', 'Description', 'Price', 'Bedrooms',
                                   'Accommodates', 'Rating'])

        #print(df)

        return df
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


