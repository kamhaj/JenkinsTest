import jaydebeapi as jdbc
import pytest
import sys

print("test script invoked")
conn_string = "jdbc:compositesw:dbapi@bdlg3207.na.pg.com:9421?domain=pg&dataSource=CIS_TST&unsupportedMode=silent"
@pytest.fixture(scope='module')
def get_fixture():
    print("This is a fixture function invoked")
	#print(str(sys.argv[1]))
    print("connecting to db 1...")
    conn = jdbc.connect("cs.jdbc.driver.CompositeDriver",       #name of the Java driver class
                        conn_string,                            #connection URL
                        [str(sys.argv[4]), str(sys.argv[5])],   			#user and password
                        "csjdbc.jar")                           #jar-Files of the driver
    print("DB 1 CONNECTION SUCCESS")
    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    yield cursor
    # disconnect from server
    print("\nclosing db connection...")



def test_success(get_fixture):
        assert 5 >= 2

def test_success_2(get_fixture):
		assert True
		
def test_fail():
		assert False
		
def test_fail_2():
		assert -3 > 15
		
		