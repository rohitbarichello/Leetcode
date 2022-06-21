def rectangleBoxes(ops):
    boxes = []
    rectangles = []
    result = []

    # get rectangles and boxes
    for op in ops:
        if op[0] == 0:
            rectangles.append(op[1:]) # so rectangles is going to hold the dimensions of added rectangles
        else:
            boxes.append(op[1:]) # boxes will hold the dimensions of current volume available

    # fill result
    for box in boxes: # each instance of box is the dimensions of the volume available for this try
        bWidth, bHeight = box

        # check if each rectangle fit in box
        willRectangleFit = True
        for rectangle in rectangles:
            rWidth, rHeight = rectangle

            # check by rotating rectangle 90 degree and without rotating
            if (rWidth > bWidth or rHeight > bHeight) and (rWidth > bHeight or rHeight > bWidth):
                willRectangleFit = False
                break

        # update result
        result.append(willRectangleFit)

    return result