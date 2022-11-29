import psycopg2
import psycopg2.extras
import pandas as pd

db_name = 'la_airbnb_412'
db_user = 'postgres'
db_password = '1301'
db_host = 'localhost'
port_id = '5432'


# Test your inputs for the query with these vars; a value of "None" means its ignored/checkboxed on the filters page
min_price1 = 50
max_price1 = 100
bedrooms1 = None
accommodates1 = 2
neighborhood1 = 'Hollywood'
checkin_date1 = '2022-12-01'
checkout_date1 = '2022-12-31'


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

        if neighborhood is not None:
            query_where += f'''AND L.description = '{neighborhood}' --these are swapped in the dbms by mistake
            '''

        query = query_select + query_where

        #print(query)
        cur.execute(query)

        df = pd.DataFrame(cur.fetchall(), columns=['Picture', 'Name', 'Neighborhood', 'Description', 'Price', 'Bedrooms', 'Accommodates', 'Rating'])

        print(df)
        print(df.loc[0, 'Picture'])

        return df
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

# Uncomment this if you'd like to test it out with the test vars above!
#execute_query(min_price1, max_price1, bedrooms1, accommodates1, neighborhood1, checkin_date1, checkout_date1)