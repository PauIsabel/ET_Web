def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}