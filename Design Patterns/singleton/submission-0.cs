public class Singleton {

    private static Singleton _instance = null;
    private string _value;

    public static Singleton getInstance() {
        _instance ??= new Singleton();
        return _instance;
    }

    public string getValue() {
        return _value;
    }

    public void setValue(string value){
        _value = value;
    }
}
