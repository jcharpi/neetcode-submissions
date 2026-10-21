public interface IObserver {
    void notify(string itemName);
}

public class Customer : IObserver {
    private string name;
    private int notifications;

    public Customer(string name) {
        this.name = name;
        this.notifications = 0;
    }

    public string getName() {
        return this.name;
    }

    public void notify(string itemName) {
        this.notifications += 1;
    }

    public int countNotifications() {
        return this.notifications;
    }
}

public class OnlineStoreItem {
    private string itemName;
    private int stock;
    private List<IObserver> _observers = new();

    public OnlineStoreItem(string itemName, int stock) {
        this.itemName = itemName;
        this.stock = stock;
    }

    public void subscribe(IObserver observer) {
        _observers.Add(observer);
    }

    public void unsubscribe(IObserver observer) {
        _observers.Remove(observer);
    }

    public void updateStock(int newStock) {
        if (this.stock == 0 && newStock > 0) {
            foreach (IObserver observer in _observers) {
                observer.notify(this.itemName);
            }
        }

        this.stock = newStock;
    }
}
