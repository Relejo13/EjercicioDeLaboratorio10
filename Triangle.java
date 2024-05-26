public class Triangle extends Figure {
    private double side1, side2, side3;

    public Triangle(String color, double side1, double side2, double side3) {
        super(color);
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    @Override
    public double perimetro() {
        return side1 + side2 + side3;
    }

    @Override
    public double area() {
        double s = perimetro() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
}
