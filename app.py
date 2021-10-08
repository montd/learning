from flask import Flask
import ghhops_server as hs
import rhino3dm
import pyclipper

app = Flask(__name__)
hops = hs.Hops(app)
@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
            hs.HopsCurve("Curve", "C", "Curve to evaluate"),
            hs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
        ], 
    outputs=[
            hs.HopsPoint("p", "p", "Point on curve at t"),
            ],
    )
def pointat(curve, t):
        return curve.PointAt(t)

if __name__ == "__main__":
    app.run()