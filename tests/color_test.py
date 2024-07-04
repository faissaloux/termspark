from termspark.painter.constants.color import Color


class TestColor:
    def test_black(self):
        assert Color.BLACK == "0,0,0"

    def test_maroon(self):
        assert Color.MAROON == "128,0,0"

    def test_green(self):
        assert Color.GREEN == "0,128,0"

    def test_olive(self):
        assert Color.OLIVE == "128,128,0"

    def test_navy(self):
        assert Color.NAVY == "0,0,128"

    def test_purple(self):
        assert Color.PURPLE == "128,0,128"

    def test_teal(self):
        assert Color.TEAL == "0,128,128"

    def test_silver(self):
        assert Color.SILVER == "192,192,192"

    def test_gray(self):
        assert Color.GRAY == "128,128,128"

    def test_grey(self):
        assert Color.GREY == "128,128,128"

    def test_red(self):
        assert Color.RED == "255,0,0"

    def test_lime(self):
        assert Color.LIME == "0,255,0"

    def test_yellow(self):
        assert Color.YELLOW == "255,255,0"

    def test_blue(self):
        assert Color.BLUE == "0,0,255"

    def test_fuchsia(self):
        assert Color.FUCHSIA == "255,0,255"

    def test_aqua(self):
        assert Color.AQUA == "0,255,255"

    def test_white(self):
        assert Color.WHITE == "255,255,255"

    def test_navy_blue(self):
        assert Color.NAVY_BLUE == "0,0,95"

    def test_dark_blue(self):
        assert Color.DARK_BLUE == "0,0,135"

    def test_dark_blue_2(self):
        assert Color.DARK_BLUE_2 == "0,0,175"

    def test_dark_blue_1(self):
        assert Color.DARK_BLUE_1 == "0,0,215"

    def test_dark_green(self):
        assert Color.DARK_GREEN == "0,95,0"

    def test_blue_stone(self):
        assert Color.BLUE_STONE == "0,95,95"

    def test_orient(self):
        assert Color.ORIENT == "0,95,135"

    def test_endeavour(self):
        assert Color.ENDEAVOUR == "0,95,175"

    def test_science_blue(self):
        assert Color.SCIENCE_BLUE == "0,95,215"

    def test_blue_ribbon(self):
        assert Color.BLUE_RIBBON == "0,95,255"

    def test_japanese_laurel(self):
        assert Color.JAPANESE_LAUREL == "0,135,0"

    def test_deep_sea(self):
        assert Color.DEEP_SEA == "0,135,95"

    def test_turquoise(self):
        assert Color.TURQUOISE == "0,135,135"

    def test_deep_cerulean(self):
        assert Color.DEEP_CERULEAN == "0,135,175"

    def test_lochmara(self):
        assert Color.LOCHMARA == "0,135,215"

    def test_azure_radiance(self):
        assert Color.AZURE_RADIANCE == "0,135,255"

    def test_islamic_green(self):
        assert Color.ISLAMIC_GREEN == "0,175,0"

    def test_spring_green(self):
        assert Color.SPRING_GREEN == "0,175,95"

    def test_dark_cyan(self):
        assert Color.DARK_CYAN == "0,175,135"

    def test_light_sea_green(self):
        assert Color.LIGHT_SEA_GREEN == "0,175,175"

    def test_cerulean(self):
        assert Color.CERULEAN == "0,175,215"

    def test_blue_bolt(self):
        assert Color.BLUE_BOLT == "0,175,255"

    def test_electric_green(self):
        assert Color.ELECTRIC_GREEN == "0,215,0"

    def test_malachite(self):
        assert Color.MALACHITE == "0,215,95"

    def test_caribbean_green(self):
        assert Color.CARIBBEAN_GREEN == "0,215,135"

    def test_cyan_1(self):
        assert Color.CYAN_1 == "0,215,175"

    def test_dark_turquoise(self):
        assert Color.DARK_TURQUOISE == "0,215,215"

    def test_vivid_sky_blue(self):
        assert Color.VIVID_SKY_BLUE == "0,215,255"

    def test_electric_green_1(self):
        assert Color.ELECTRIC_GREEN_1 == "0,255,0"

    def test_guppie_green(self):
        assert Color.GUPPIE_GREEN == "0,255,95"

    def test_spring_green_1(self):
        assert Color.SPRING_GREEN_1 == "0,255,135"

    def test_medium_spring_green(self):
        assert Color.MEDIUM_SPRING_GREEN == "0,255,175"

    def test_sea_green(self):
        assert Color.SEA_GREEN == "0,255,215"

    def test_cyan(self):
        assert Color.CYAN == "0,255,255"

    def test_rosewood(self):
        assert Color.ROSEWOOD == "95,0,0"

    def test_pompadour(self):
        assert Color.POMPADOUR == "95,0,95"

    def test_pigment_indigo(self):
        assert Color.PIGMENT_INDIGO == "95,0,135"

    def test_purple_3(self):
        assert Color.PURPLE_3 == "95,0,175"

    def test_electic_violet(self):
        assert Color.ELECTIC_VIOLET == "95,0,215"

    def test_blue_violet(self):
        assert Color.BLUE_VIOLET == "95,0,255"

    def test_verdun_green(self):
        assert Color.VERDUN_GREEN == "95,95,0"

    def test_scorpion(self):
        assert Color.SCORPION == "95,95,95"

    def test_comet(self):
        assert Color.COMET == "95,95,135"

    def test_scampi(self):
        assert Color.SCAMPI == "95,95,175"

    def test_indigo(self):
        assert Color.INDIGO == "95,95,215"

    def test_cornflower_blue_1(self):
        assert Color.CORNFLOWER_BLUE_1 == "95,95,255"

    def test_limeade(self):
        assert Color.LIMEADE == "95,135,0"

    def test_glade_green(self):
        assert Color.GLADE_GREEN == "95,135,95"

    def test_juniper(self):
        assert Color.JUNIPER == "95,135,135"

    def test_hippie_blue(self):
        assert Color.HIPPIE_BLUE == "95,135,175"

    def test_havelock_blue(self):
        assert Color.HAVELOCK_BLUE == "95,135,215"

    def test_cornflower_blue(self):
        assert Color.CORNFLOWER_BLUE == "95,135,255"

    def test_limea(self):
        assert Color.LIMEA == "95,175,0"

    def test_fern(self):
        assert Color.FERN == "95,175,95"

    def test_silver_tree(self):
        assert Color.SILVER_TREE == "95,175,135"

    def test_tradewind(self):
        assert Color.TRADEWIND == "95,175,175"

    def test_shakespeare(self):
        assert Color.SHAKESPEARE == "95,175,215"

    def test_malibu(self):
        assert Color.MALIBU == "95,175,255"

    def test_bright_green(self):
        assert Color.BRIGHT_GREEN == "95,215,0"

    def test_pale_green(self):
        assert Color.PALE_GREEN == "95,215,95"

    def test_pastel_green(self):
        assert Color.PASTEL_GREEN == "95,215,135"

    def test_downy(self):
        assert Color.DOWNY == "95,215,175"

    def test_viking(self):
        assert Color.VIKING == "95,215,215"

    def test_steel_blue(self):
        assert Color.STEEL_BLUE == "95,215,255"

    def test_chartreuse(self):
        assert Color.CHARTREUSE == "95,255,0"

    def test_screaming_green(self):
        assert Color.SCREAMING_GREEN == "95,255,95"

    def test_sea_green_1(self):
        assert Color.SEA_GREEN_1 == "95,255,135"

    def test_aquamarine_1(self):
        assert Color.AQUAMARINE_1 == "95,255,175"

    def test_aquamarine_2(self):
        assert Color.AQUAMARINE_2 == "95,255,215"

    def test_aquamarine(self):
        assert Color.AQUAMARINE == "95,255,255"

    def test_dark_red(self):
        assert Color.DARK_RED == "135,0,0"

    def test_fresh_eggplant(self):
        assert Color.FRESH_EGGPLANT == "135,0,95"

    def test_dark_magenta(self):
        assert Color.DARK_MAGENTA == "135,0,135"

    def test_purple_2(self):
        assert Color.PURPLE_2 == "135,0,175"

    def test_electric_violet(self):
        assert Color.ELECTRIC_VIOLET == "135,0,215"

    def test_purple_1(self):
        assert Color.PURPLE_1 == "135,0,255"

    def test_brown(self):
        assert Color.BROWN == "135,95,0"

    def test_copper_rose(self):
        assert Color.COPPER_ROSE == "135,95,95"

    def test_strike_master(self):
        assert Color.STRIKE_MASTER == "135,95,135"

    def test_deluge(self):
        assert Color.DELUGE == "135,95,175"

    def test_medium_purple(self):
        assert Color.MEDIUM_PURPLE == "135,95,215"

    def test_heliotrope(self):
        assert Color.HELIOTROPE == "135,95,255"

    def test_olive_1(self):
        assert Color.OLIVE_1 == "135,135,0"

    def test_clay_creek(self):
        assert Color.CLAY_CREEK == "135,135,95"

    def test_gray_1(self):
        assert Color.GRAY_1 == "135,135,135"

    def test_grey_1(self):
        assert Color.GREY_1 == "135,135,135"

    def test_wild_blue_yonder(self):
        assert Color.WILD_BLUE_YONDER == "135,135,175"

    def test_chetwode_blue(self):
        assert Color.CHETWODE_BLUE == "135,135,215"

    def test_light_slate_blue(self):
        assert Color.LIGHT_SLATE_BLUE == "135,135,255"

    def test_limeade_1(self):
        assert Color.LIMEADE_1 == "135,175,0"

    def test_chelsea_cucumber(self):
        assert Color.CHELSEA_CUCUMBER == "135,175,95"

    def test_bay_leaf(self):
        assert Color.BAY_LEAF == "135,175,135"

    def test_gulf_stream(self):
        assert Color.GULF_STREAM == "135,175,175"

    def test_polo_blue(self):
        assert Color.POLO_BLUE == "135,175,215"

    def test_malibu_1(self):
        assert Color.MALIBU_1 == "135,175,255"

    def test_pistachio(self):
        assert Color.PISTACHIO == "135,215,0"

    def test_dark_olive_green(self):
        assert Color.DARK_OLIVE_GREEN == "135,215,95"

    def test_feijoa(self):
        assert Color.FEIJOA == "135,215,135"

    def test_vista_blue(self):
        assert Color.VISTA_BLUE == "135,215,175"

    def test_bermuda(self):
        assert Color.BERMUDA == "135,215,215"

    def test_anakiwa(self):
        assert Color.ANAKIWA == "135,215,255"

    def test_chartreuse_1(self):
        assert Color.CHARTREUSE_1 == "135,255,0"

    def test_light_green(self):
        assert Color.LIGHT_GREEN == "135,255,95"

    def test_mstr_green(self):
        assert Color.Mstr_GREEN == "135,255,135"

    def test_pale_green_1(self):
        assert Color.PALE_GREEN_1 == "135,255,175"

    def test_aqua_marine(self):
        assert Color.AQUA_MARINE == "135,255,215"

    def test_anakiwa_1(self):
        assert Color.ANAKIWA_1 == "135,255,255"

    def test_bright_red(self):
        assert Color.BRIGHT_RED == "175,0,0"

    def test_flirt(self):
        assert Color.FLIRT == "175,0,95"

    def test_medium_violet_red(self):
        assert Color.MEDIUM_VIOLET_RED == "175,0,135"

    def test_magenta_1(self):
        assert Color.MAGENTA_1 == "175,0,175"

    def test_dark_violet(self):
        assert Color.DARK_VIOLET == "175,0,215"

    def test_purple_4(self):
        assert Color.PURPLE_4 == "175,0,255"

    def test_rose_of_sharon(self):
        assert Color.ROSE_OF_SHARON == "175,95,0"

    def test_indian_red(self):
        assert Color.INDIAN_RED == "175,95,95"

    def test_tapestry(self):
        assert Color.TAPESTRY == "175,95,135"

    def test_fuchsia_pink(self):
        assert Color.FUCHSIA_PINK == "175,95,175"

    def test_medium_purple_1(self):
        assert Color.MEDIUM_PURPLE_1 == "175,95,215"

    def test_heliotrope_1(self):
        assert Color.HELIOTROPE_1 == "175,95,255"

    def test_pirate_gold(self):
        assert Color.PIRATE_GOLD == "175,135,0"

    def test_muesli(self):
        assert Color.MUESLI == "175,135,95"

    def test_pharlap(self):
        assert Color.PHARLAP == "175,135,135"

    def test_bouquet(self):
        assert Color.BOUQUET == "175,135,175"

    def test_lavender(self):
        assert Color.LAVENDER == "175,135,215"

    def test_heliotrope_2(self):
        assert Color.HELIOTROPE_2 == "175,135,255"

    def test_gold_1(self):
        assert Color.GOLD_1 == "175,175,0"

    def test_olive_green(self):
        assert Color.OLIVE_GREEN == "175,175,95"

    def test_hillary(self):
        assert Color.HILLARY == "175,175,135"

    def test_silver_chalice(self):
        assert Color.SILVER_CHALICE == "175,175,175"

    def test_wistful(self):
        assert Color.WISTFUL == "175,175,215"

    def test_melrose(self):
        assert Color.MELROSE == "175,175,255"

    def test_rio_grande(self):
        assert Color.RIO_GRANDE == "175,215,0"

    def test_conifer(self):
        assert Color.CONIFER == "175,215,95"

    def test_feijoa_1(self):
        assert Color.FEIJOA_1 == "175,215,135"

    def test_pixie_green(self):
        assert Color.PIXIE_GREEN == "175,215,175"

    def test_jungle_mist(self):
        assert Color.JUNGLE_MIST == "175,215,215"

    def test_anakiwa_2(self):
        assert Color.ANAKIWA_2 == "175,215,255"

    def test_lime_1(self):
        assert Color.LIME_1 == "175,255,0"

    def test_green_yellow(self):
        assert Color.GREEN_YELLOW == "175,255,95"

    def test_mstr_green_1(self):
        assert Color.Mstr_GREEN_1 == "175,255,135"

    def test_dark_sea_green(self):
        assert Color.DARK_SEA_GREEN == "175,255,175"

    def test_aero_blue(self):
        assert Color.AERO_BLUE == "175,255,215"

    def test_french_pass(self):
        assert Color.FRENCH_PASS == "175,255,255"

    def test_guardsman_red(self):
        assert Color.GUARDSMAN_RED == "215,0,0"

    def test_razzmatazz(self):
        assert Color.RAZZMATAZZ == "215,0,95"

    def test_hollywood_cerise(self):
        assert Color.HOLLYWOOD_CERISE == "215,0,135"

    def test_hollywood_cerise_1(self):
        assert Color.HOLLYWOOD_CERISE_1 == "215,0,175"

    def test_purple_pizzazz(self):
        assert Color.PURPLE_PIZZAZZ == "215,0,215"

    def test_electric_violet_1(self):
        assert Color.ELECTRIC_VIOLET_1 == "215,0,255"

    def test_tenn(self):
        assert Color.TENN == "215,95,0"

    def test_roman(self):
        assert Color.ROMAN == "215,95,95"

    def test_cranberry(self):
        assert Color.CRANBERRY == "215,95,135"

    def test_hopbush(self):
        assert Color.HOPBUSH == "215,95,175"

    def test_orchid(self):
        assert Color.ORCHID == "215,95,215"

    def test_medium_orchid(self):
        assert Color.MEDIUM_ORCHID == "215,95,255"

    def test_mango_tango(self):
        assert Color.MANGO_TANGO == "215,135,0"

    def test_copperfield(self):
        assert Color.COPPERFIELD == "215,135,95"

    def test_pink(self):
        assert Color.PINK == "215,135,135"

    def test_cancan(self):
        assert Color.CANCAN == "215,135,175"

    def test_light_orchid(self):
        assert Color.LIGHT_ORCHID == "215,135,215"

    def test_heliotrope_3(self):
        assert Color.HELIOTROPE_3 == "215,135,255"

    def test_corn(self):
        assert Color.CORN == "215,175,0"

    def test_tacha(self):
        assert Color.TACHA == "215,175,95"

    def test_tan(self):
        assert Color.TAN == "215,175,135"

    def test_clam_shell(self):
        assert Color.CLAM_SHELL == "215,175,175"

    def test_thistle(self):
        assert Color.THISTLE == "215,175,215"

    def test_mauve(self):
        assert Color.MAUVE == "215,175,255"

    def test_corn_1(self):
        assert Color.CORN_1 == "215,215,0"

    def test_khaki(self):
        assert Color.KHAKI == "215,215,95"

    def test_deco(self):
        assert Color.DECO == "215,215,135"

    def test_green_mist(self):
        assert Color.GREEN_MIST == "215,215,175"

    def test_alto(self):
        assert Color.ALTO == "215,215,215"

    def test_fog(self):
        assert Color.FOG == "215,215,255"

    def test_chartreuse_yellow(self):
        assert Color.CHARTREUSE_YELLOW == "215,255,0"

    def test_canary(self):
        assert Color.CANARY == "215,255,95"

    def test_honeysuckle(self):
        assert Color.HONEYSUCKLE == "215,255,135"

    def test_reef(self):
        assert Color.REEF == "215,255,175"

    def test_snowy_mstr(self):
        assert Color.SNOWY_Mstr == "215,255,215"

    def test_oyster_bay(self):
        assert Color.OYSTER_BAY == "215,255,255"

    def test_rose(self):
        assert Color.ROSE == "255,0,95"

    def test_deep_pink(self):
        assert Color.DEEP_PINK == "255,0,135"

    def test_hollywood_cerise_2(self):
        assert Color.HOLLYWOOD_CERISE_2 == "255,0,175"

    def test_purple_pizzazz_1(self):
        assert Color.PURPLE_PIZZAZZ_1 == "255,0,215"

    def test_magenta(self):
        assert Color.MAGENTA == "255,0,255"

    def test_blaze_orange(self):
        assert Color.BLAZE_ORANGE == "255,95,0"

    def test_bitter_sweet(self):
        assert Color.BITTER_SWEET == "255,95,95"

    def test_wild_watermelon(self):
        assert Color.WILD_WATERMELON == "255,95,135"

    def test_hotpink(self):
        assert Color.HOTPINK == "255,95,175"

    def test_hotpink_1(self):
        assert Color.HOTPINK_1 == "255,95,215"

    def test_pink_flamingo(self):
        assert Color.PINK_FLAMINGO == "255,95,255"

    def test_flush_orange(self):
        assert Color.FLUSH_ORANGE == "255,135,0"

    def test_salmon(self):
        assert Color.SALMON == "255,135,95"

    def test_vivid_tangerine(self):
        assert Color.VIVID_TANGERINE == "255,135,135"

    def test_pink_salmon(self):
        assert Color.PINK_SALMON == "255,135,175"

    def test_lavender_rose(self):
        assert Color.LAVENDER_ROSE == "255,135,215"

    def test_blush_pink(self):
        assert Color.BLUSH_PINK == "255,135,255"

    def test_yellow_sea(self):
        assert Color.YELLOW_SEA == "255,175,0"

    def test_texas_rose(self):
        assert Color.TEXAS_ROSE == "255,175,95"

    def test_hit_pink(self):
        assert Color.HIT_PINK == "255,175,135"

    def test_sundown(self):
        assert Color.SUNDOWN == "255,175,175"

    def test_cotton_candy(self):
        assert Color.COTTON_CANDY == "255,175,215"

    def test_lavender_rose_1(self):
        assert Color.LAVENDER_ROSE_1 == "255,175,255"

    def test_gold(self):
        assert Color.GOLD == "255,215,0"

    def test_dandelion(self):
        assert Color.DANDELION == "255,215,95"

    def test_grandis(self):
        assert Color.GRANDIS == "255,215,135"

    def test_caramel(self):
        assert Color.CARAMEL == "255,215,175"

    def test_cosmos(self):
        assert Color.COSMOS == "255,215,215"

    def test_pink_lace(self):
        assert Color.PINK_LACE == "255,215,255"

    def test_laser_lemon(self):
        assert Color.LASER_LEMON == "255,255,95"

    def test_dolly(self):
        assert Color.DOLLY == "255,255,135"

    def test_portafino(self):
        assert Color.PORTAFINO == "255,255,175"

    def test_cumulus(self):
        assert Color.CUMULUS == "255,255,215"

    def test_cod_gray(self):
        assert Color.COD_GRAY == "8,8,8"

    def test_cod_gray_1(self):
        assert Color.COD_GRAY_1 == "18,18,18"

    def test_cod_gray_2(self):
        assert Color.COD_GRAY_2 == "28,28,28"

    def test_mine_shaft(self):
        assert Color.MINE_SHAFT == "38,38,38"

    def test_mine_shaft_1(self):
        assert Color.MINE_SHAFT_1 == "48,48,48"

    def test_mine_shaft_2(self):
        assert Color.MINE_SHAFT_2 == "58,58,58"

    def test_tundora(self):
        assert Color.TUNDORA == "68,68,68"

    def test_tundora_1(self):
        assert Color.TUNDORA_1 == "78,78,78"

    def test_scorpion_1(self):
        assert Color.SCORPION_1 == "88,88,88"

    def test_dove_gray(self):
        assert Color.DOVE_GRAY == "98,98,98"

    def test_dove_gray_1(self):
        assert Color.DOVE_GRAY_1 == "108,108,108"

    def test_boulder(self):
        assert Color.BOULDER == "118,118,118"

    def test_gray_2(self):
        assert Color.GRAY_2 == "138,138,138"

    def test_grey_2(self):
        assert Color.GREY_2 == "138,138,138"

    def test_dusty_gray(self):
        assert Color.DUSTY_GRAY == "148,148,148"

    def test_silver_chalice_1(self):
        assert Color.SILVER_CHALICE_1 == "158,158,158"

    def test_silver_chalice_2(self):
        assert Color.SILVER_CHALICE_2 == "168,168,168"

    def test_silver_chalice_3(self):
        assert Color.SILVER_CHALICE_3 == "178,178,178"

    def test_silver_1(self):
        assert Color.SILVER_1 == "188,188,188"

    def test_silver_2(self):
        assert Color.SILVER_2 == "198,198,198"

    def test_alto_1(self):
        assert Color.ALTO_1 == "208,208,208"

    def test_alto_2(self):
        assert Color.ALTO_2 == "218,218,218"

    def test_mercury(self):
        assert Color.MERCURY == "228,228,228"

    def test_gallery(self):
        assert Color.GALLERY == "238,238,238"
