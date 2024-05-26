public abstract class Figure {
    protected String color;

    public Figure(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double perimetro();
    public abstract double area();
}