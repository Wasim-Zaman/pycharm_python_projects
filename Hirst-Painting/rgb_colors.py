class RGBColors():
    def get_rgb_colors(self, colorgram_obj):
        '''
        Returns the list of rgb colors
        :param colorgram_obj:
        :return list_of_rgb_colots:
        '''
        list_of_rgb_colors = []

        # visiting each and every color in colorgram
        for color in colorgram_obj:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            list_of_rgb_colors.append((r, g, b))

        return list_of_rgb_colors