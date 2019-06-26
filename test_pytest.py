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
		
def test_success_3(get_fixture):
		assert True

def test_success_4(get_fixture):
		assert True

def test_success_5(get_fixture):
		assert True

def test_success_6(get_fixture):
		assert True

def test_success_7(get_fixture):
		assert True

def test_success_8(get_fixture):
		assert True

def test_success_9(get_fixture):
		assert True

def test_success_10(get_fixture):
		assert True

def test_success_11(get_fixture):
		assert True

def test_success_12(get_fixture):
		assert True

def test_success_13(get_fixture):
		assert True

def test_success_14(get_fixture):
		assert True

def test_success_15(get_fixture):
		assert True

def test_success_16(get_fixture):
		assert True

def test_success_17(get_fixture):
		assert True

def test_success_18(get_fixture):
		assert True	
		
def test_success_19(get_fixture):
		assert True
		
def test_success_20(get_fixture):
		assert True