#!/usr/bin/env python3
"""Build proposed order and Exhibit A PDFs for 25-12729-393."""

from fpdf import FPDF


CAUSE = "NO. 25-12729-393"


class Doc(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Times", "I", 9)
        self.cell(0, 8, "Cause No. 25-12729-393  |  Eldomiaty v. Soh  |  393rd District Court", align="C")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 9)
        self.cell(0, 8, f"Page {self.page_no()} of {{nb}}", align="C")


def caption(pdf):
    pdf.set_font("Times", "B", 12)
    pdf.cell(0, 6, CAUSE, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Times", "B", 11)
    for line in [
        "IN THE MATTER OF THE MARRIAGE OF",
        "NYERA ELDOMIATY AND ANDREW KHENG BEE SOH",
        "IN THE 393RD JUDICIAL DISTRICT COURT",
        "DENTON COUNTY, TEXAS",
    ]:
        pdf.cell(0, 5.5, line, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)


def body(pdf, text):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Times", "", 11)
    pdf.multi_cell(0, 5.5, text)
    pdf.ln(1)


def heading(pdf, text):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Times", "B", 11)
    pdf.cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def bullet(pdf, text):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Times", "", 11)
    pdf.cell(8, 5.5, "-")
    pdf.multi_cell(0, 5.5, text)
    pdf.set_x(pdf.l_margin)


def build_order(path):
    pdf = Doc(format="Letter")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    caption(pdf)
    pdf.set_font("Times", "B", 12)
    pdf.multi_cell(
        0,
        6,
        "ORDER ON PETITIONER'S MOTION FOR NEW TRIAL\nAND TO MODIFY, CORRECT, OR REFORM THE DECREE",
        align="C",
    )
    pdf.ln(4)
    body(
        pdf,
        "On the date signed below, the Court considered Petitioner's Motion for New Trial "
        "and to Modify, Correct, or Reform the Decree, filed November 16, 2026. Petitioner, "
        "Nyera Eldomiaty, appeared pro se. Respondent, Andrew Kheng Bee Soh, was served "
        "with the motion.",
    )
    body(
        pdf,
        "The Court finds that the Final Decree of Divorce signed October 16, 2026, did not "
        "expressly award Petitioner her clothing, furniture, household goods, and personal "
        "belongings remaining at Respondent's residence. The Court finds that reforming the "
        "decree as to that property is just and right, and that the divorce itself and the "
        "safety provisions already in the decree should remain in effect.",
    )
    heading(pdf, "IT IS ORDERED:")
    body(
        pdf,
        "1. Petitioner's Motion is GRANTED in part. The Court reforms the property division "
        "in the Final Decree of Divorce signed October 16, 2026, as stated in this Order. "
        "The divorce granted in that Decree remains in effect. This Order does not reopen "
        "or set aside the divorce.",
    )
    body(
        pdf,
        "2. Petitioner is awarded as her sole and separate property, and Respondent is "
        "divested of all right, title, interest, and claim to the property described in "
        "Exhibit A, including any supplement filed before the hearing, and specifically to:"
    )
    for item in [
        "all clothing, jewelry, personal effects, furniture, household goods, and belongings of Petitioner that are at Respondent's residence or in Respondent's possession, including the items listed in Exhibit A;",
        "Petitioner's cat and all pet-related property;",
        "Petitioner's legal, identification, immigration, medical, financial, tax, insurance, employment, family, and sentimental records and documents;",
        "Petitioner's phones, computers, tablets, chargers, drives, and digital accounts and contents belonging to Petitioner;",
        "all other personal property belonging to Petitioner, whether now in Petitioner's possession or later recovered.",
    ]:
        bullet(pdf, item)
    pdf.ln(1)
    body(
        pdf,
        "3. The cat, pet-related property, Petitioner's records, and Petitioner's identity "
        "documents remain awarded to Petitioner as stated in the October 16, 2026 Decree.",
    )
    body(
        pdf,
        "4. Any retrieval or exchange of property awarded to Petitioner shall occur only "
        "through law enforcement, a constable or sheriff, civil standby, a licensed attorney, "
        "a court-approved neutral, or another method approved in writing by this Court. "
        "Petitioner is not required to meet Respondent, go to Respondent's residence, or "
        "disclose Petitioner's location. Respondent shall not be present at Petitioner's "
        "location. No-contact and protective-order rules control any retrieval.",
    )
    body(
        pdf,
        "5. Respondent shall not hide, damage, transfer, sell, or interfere with property "
        "awarded to Petitioner. Respondent shall make that property available for retrieval "
        "under paragraph 4 within fourteen (14) days of this Order, or on the date set by "
        "the constable, sheriff, or civil-standby officer.",
    )
    body(
        pdf,
        "6. Petitioner's residential address, telephone number, workplace, and safe location "
        "shall not be stated in this Order and shall remain confidential. Petitioner may be "
        "contacted only through email at eldomiatyn@yahoo.com or through the District Clerk.",
    )
    body(
        pdf,
        "7. Nothing in this Order modifies, reduces, limits, or replaces any protective order, "
        "temporary ex parte protective order, emergency protection order, bond condition, "
        "criminal no-contact order, or other safety order. If any part of this Order conflicts "
        "with a more protective order, the more protective order controls.",
    )
    body(
        pdf,
        "8. All other relief requested in the Motion and not granted in this Order is denied.",
    )
    pdf.ln(8)
    pdf.set_font("Times", "", 11)
    pdf.cell(0, 6, "SIGNED on _________________________, 2026.", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(16)
    pdf.cell(0, 6, "_________________________________", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Times", "B", 11)
    pdf.cell(0, 6, "JUDGE PRESIDING", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Times", "", 10)
    pdf.multi_cell(
        0,
        5,
        "APPROVED AS TO FORM:\n\n"
        "_________________________________\n"
        "Nyera Eldomiaty, Petitioner, Pro Se\n"
        "eldomiatyn@yahoo.com\n"
        "Address and phone confidential, on file with the District Clerk",
    )
    pdf.output(path)


def sign_block(pdf):
    pdf.ln(6)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Times", "", 11)
    pdf.cell(0, 6, "Respectfully submitted,", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.cell(0, 6, "_________________________________", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Nyera Eldomiaty, Petitioner, Pro Se", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "eldomiatyn@yahoo.com", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Address and phone confidential, on file with the District Clerk", new_x="LMARGIN", new_y="NEXT")


def build_exhibit(path):
    pdf = Doc(format="Letter")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    caption(pdf)
    pdf.set_font("Times", "B", 12)
    pdf.multi_cell(0, 6, "EXHIBIT A\nPETITIONER'S PROPERTY LIST", align="C")
    pdf.ln(3)
    body(
        pdf,
        "This list identifies property Petitioner asks the Court to award to her and to allow "
        "to be retrieved from Respondent's residence, 4400 Coney Island Drive, Frisco, Texas "
        "75036, only through a constable, sheriff, or civil standby, with movers present so "
        "the retrieval is one trip. Property is stored in the guest bedroom, garage, and "
        "closet, including wrapped furniture and sealed boxes, and also in other rooms shown "
        "in photographs. Petitioner asks for every item belonging to her in those locations, "
        "not only the items already photographed.",
    )
    heading(pdf, "How retrieval should work")
    body(
        pdf,
        "One civil-standby or constable date. Movers load from the guest bedroom, garage, "
        "closet, and any other room where Petitioner's property is kept. Wrapped furniture "
        "and boxes marked as Petitioner's are taken intact. Petitioner is not present at "
        "Respondent's residence. Respondent is not present at the load-out.",
    )
    heading(pdf, "Locations at 4400 Coney Island Drive, Frisco, Texas 75036")
    body(
        pdf,
        "Guest bedroom: furniture, boxes, and personal belongings of Petitioner, including "
        "items still wrapped or packed.",
    )
    body(
        pdf,
        "Garage: wrapped furniture, boxed household goods, and other property of Petitioner "
        "stored there.",
    )
    body(
        pdf,
        "Closet: clothing, packed belongings, and other property of Petitioner.",
    )
    body(
        pdf,
        "Other rooms: dresser, mirror, clothing, bags, toiletries, hair tools, and personal "
        "effects shown in Petitioner's photographs, and any other property of Petitioner in "
        "the residence.",
    )
    heading(pdf, "Specific items shown in earlier photographs (A-1 and following)")
    items = [
        "1. Dark wood dresser.",
        "2. White-framed rectangular mirror.",
        "3. Blue and purple hair dryer with round diffuser, cords, and black cases.",
        "4. White and rose-gold styling tool.",
        "5. Blue cordless landline phone.",
        "6. Navy blood-pressure cuff.",
        "7. White drawer with wood organizer insert.",
        "8. White athletic shoes.",
        "9. Clothing on the floor and in piles, including jeans, shirts, socks, and a red garment with gold pattern.",
        "10. Bras in a clear bag.",
        "11. Black duffel bag, blue tote bag, black drawstring bag, and makeup cases.",
        "12. Baskets, boxes, and containers of toiletries, hair products, medication bottles, and personal-care items.",
    ]
    pdf.set_font("Times", "", 11)
    for line in items:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5.5, line)
    pdf.ln(2)
    heading(pdf, "Supplement from Petitioner's photographs IMG_0442 through IMG_0534 (92 photos)")
    body(
        pdf,
        "These photographs show Petitioner's packed clothing, labeled Home Depot boxes, "
        "closet, bathroom products, kitchenware, and living-room goods at Respondent's "
        "residence. Labels on bags and boxes are Petitioner's handwriting. Counts on labels "
        "are Petitioner's counts of pieces in that bag or box. Petitioner asks for every "
        "item in those photographs and every matching unlabeled piece in the same rooms.",
    )
    heading(pdf, "Closet, hanging clothes, and packed clothing")
    for line in [
        "13. Full closet of Petitioner's hanging clothes, many in clear garment bags, including jackets, coats, puffer coat, dresses, tops, and pants; shoes on the upper shelf; extra hangers on the lower rod. Photos IMG_0444, IMG_0445, IMG_0446.",
        "14. Four brown wicker baskets of folded jeans and folded clothing on a dark carved-wood cabinet, with a table lamp. Photo IMG_0442.",
        "15. Home Depot medium box labeled: Outerwear; Shorts; NS Button downs; Turtlenecks; Short sleeve & sweaters; BS, CS, CT. Photo IMG_0455.",
        "16. Garment bag labeled: BLAZERS, SWEATERS, JEAN JACKETS AND VESTS - 15. Photo IMG_0457.",
        "17. Home Depot box labeled: Trousers B, S, JJ, V. Photo IMG_0458.",
        "18. Home Depot box labeled: NS BBB Dresses; NS G, P, R, Pii, O, Y, C, A dresses. Photos IMG_0462 through IMG_0466.",
        "19. Home Depot box labeled: Skirts; NS E SS; Sq pants & skirts; Hoodies; 5 Gilets. Photo IMG_0474.",
        "20. Home Depot box labeled: S work buttons; S short sleeve and sleeveless tops; E SS work tops & button-down sleeveless tops; S LS tops; S LS sweaters; S jumpers. Photos IMG_0482, IMG_0483.",
        "21. Home Depot box labeled: C.S. sleeveless & SS dresses; C.S. long-sleeve dresses; S evening dresses; coverups. Photos IMG_0492, IMG_0493.",
        "22. Labeled garment bags and wrapped bundles, including: shorts (25); Express spaghetti-strap tops; synthetic pants and skirts; synthetic belts (7); synthetic work buttons (15); synthetic short-sleeve and sleeveless tops (21); Express short-sleeve work tops and button-down sleeveless tops (6); synthetic long-sleeve tops; synthetic long-sleeve sweaters (8); synthetic jumpers (7); casual synthetic sleeveless and short-sleeve dresses (20); synthetic midi and maxi dresses (20 and 4); synthetic jackets and cardigans (9); bridesmaid dresses (9); coverups (4); long-sleeve hoodies; button-down shirts (11); outerwear (12); turtlenecks (6). Photos IMG_0447 through IMG_0499 and further photographs sent November 22, 2026.",
    ]:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", "", 11)
        pdf.multi_cell(0, 5.5, line)
        pdf.ln(0.4)
    heading(pdf, "Bathroom and personal-care items")
    body(
        pdf,
        "23. Clear organizer bin and round spinner of Petitioner's toiletries and cosmetics "
        "on the bathroom counter, including Bath & Body Works lotions and body sprays, "
        "Honest products, Clinelle mask, and other bottles and tubes. Photo IMG_0443.",
    )
    heading(pdf, "Kitchen, cookware, and appliances")
    for line in [
        "24. Blue enameled Dutch oven (labeled on the box as huge Dutch oven). Photos IMG_0501, IMG_0517 through IMG_0520, IMG_0525.",
        "25. Home Depot box labeled: Cake pan; air fryer; tupperware; pans. Photos IMG_0503 through IMG_0511.",
        "26. Bakeware and cookware photographed with that box, including muffin tins, loaf pan, griddle/grill pan, steamer or rice-cooker insert, pots, lids, and plastic storage. Photos IMG_0503 through IMG_0510.",
        "27. Home Depot box labeled: Huge Dutch oven; Water heater; cake tray; 5 pans; 2 plastic with drawers. Contents shown include the Dutch oven, electric kettles, travel mug, boxed mix, and pans. Photos IMG_0517 through IMG_0525.",
        "28. Kitchen appliances and serving pieces: electric kettle, toaster or small appliance, white cake stand, blender or similar, and related items on the counter and in boxes. Photos IMG_0512, IMG_0518 through IMG_0521.",
        "29. Dishes, bowls, plates, cups, glassware, and food-storage containers in the photographed cabinets and boxes. Photos IMG_0501, IMG_0502, IMG_0514 through IMG_0516, IMG_0526, IMG_0527.",
        "30. Paper goods, foil, and boxed kitchen supplies in an open carton. Photo IMG_0526.",
    ]:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", "", 11)
        pdf.multi_cell(0, 5.5, line)
        pdf.ln(0.4)
    heading(pdf, "Living room, decor, and hardware")
    for line in [
        "31. Home Depot medium box labeled Living Room: books; candles; vase; trash; green shelves brackets & screws. Photos IMG_0530, IMG_0531.",
        "32. Glass vase with white flowers, glassware, and a wood tray. Photo IMG_0529.",
        "33. Dark marble or glass board or tabletop. Photo IMG_0532.",
        "34. Black wall television mount and cables. Photos IMG_0533, IMG_0534.",
        "35. All other Home Depot boxes, garment bags, hangers, and packed belongings of Petitioner shown in IMG_0442 through IMG_0534, whether or not the label is fully readable.",
    ]:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", "", 11)
        pdf.multi_cell(0, 5.5, line)
        pdf.ln(0.4)
    heading(pdf, "Further photographs sent November 22, 2026")
    for line in [
        "36. Garment bag labeled BUTTON DOWN SHIRTS - 11.",
        "37. Garment bag labeled OUTERWEAR - 12, including polka-dot and beige pieces.",
        "38. Garment bag labeled TURTLENECKS - 6.",
        "39. Closet shelves stacked with folded shirts, pants, and shoes, plus hanging clothes; bathroom visible through the doorway.",
        "40. Teal laundry basket and contents; white sneaker and dark sneaker; gray tufted bench.",
        "41. Bedroom set: bed with white comforter and pillows; dark wood nightstand; silver lamp with white shade.",
        "42. Dark writing desk.",
        "43. Patterned area rug; cat figure-8 track toy, wand toy, bowls, green container, and black automatic litter box. These are pet-related property awarded with the cat.",
        "44. Cast-iron or hard-anodized griddle, white cutting board, wood cutting board, metal baking sheet, and steamer basket.",
        "45. Black pots, pans, lids, and saucepan in the cabinet.",
        "46. Open carton with black air fryer, teal-lid containers, glass dishes, wooden cake stand, and patterned linens.",
        "47. Cabinet of glass food-storage containers and lids (teal, green, blue) and a patterned ceramic canister.",
        "48. White square dinner plates, white bowls, and a patterned plate.",
        "49. Under-sink cleaning supplies photographed by Petitioner, including Glad ForceFlex bags and Cascade dishwasher pods.",
        "50. Wool dryer balls in the dryer.",
        "51. Bathroom vanity items: foaming soap, glitter soap pump, green toothbrush.",
        "52. Bathroom shower accessories (photo is motion-blurred).",
        "53. Tool shelf: screwdriver set, red lantern, Ryobi drill and case, and boxed hardware.",
        "54. Living room: sofa, yellow coffee table, brown pouf, wall art, ceiling fan, full-length wood-framed floor mirror, vase with flowers in the niche, robot vacuum, and bags on the floor.",
        "55. Black wall television mount (close photograph of the bracket).",
    ]:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", "", 11)
        pdf.multi_cell(0, 5.5, line)
        pdf.ln(0.4)
    heading(pdf, "Category awards requested")
    cats = [
        "A. All of Petitioner's clothing, shoes, jewelry, and personal effects at Respondent's residence, whether or not separately photographed, including every labeled bag and box in the closet photographs.",
        "B. All furniture and household goods belonging to Petitioner at Respondent's residence, including the dresser, bed and white bedding, nightstand, lamp, desk, tufted bench, area rug, sofa, coffee table, pouf, full-length wood-framed floor mirror, carved-wood cabinet, green shelves and brackets, television mount, robot vacuum, and any other furniture, furnishings, or household items that are Petitioner's.",
        "C. Toiletries, cosmetics, hair tools and products, and medications belonging to Petitioner.",
        "D. Kitchenware belonging to Petitioner: Dutch oven, air fryer, pans, bakeware, Tupperware and food storage, dishes, glassware, kettles, and small appliances.",
        "E. Petitioner's cat and all pet-related property, including the automatic litter box, toys, bowls, veterinary records, microchip registration, medications, food, litter, carriers, and supplies.",
        "F. Petitioner's records and identity documents, including legal, identification, immigration, medical, financial, tax, insurance, employment, family, and sentimental records, and books packed in the Living Room box.",
        "G. Phones, computers, tablets, chargers, drives, and digital accounts and contents belonging to Petitioner.",
        "H. All other personal property belonging to Petitioner at Respondent's residence or in Respondent's possession.",
    ]
    for line in cats:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5.5, line)
        pdf.ln(0.5)
    pdf.ln(2)
    heading(pdf, "Retrieval")
    body(
        pdf,
        "Petitioner is not required to meet Respondent or go to Respondent's residence. "
        "Retrieval shall occur only through law enforcement, a constable or sheriff, civil "
        "standby, or another method approved in writing by the Court. Packed boxes and "
        "garment bags are to be taken intact so the load-out is one trip.",
    )
    heading(pdf, "Photographs")
    body(
        pdf,
        "Exhibit A-1 and following are the earlier photographs of the dresser, mirror, hair "
        "dryer, phone, blood-pressure cuff, clothing, bags, and toiletries. Exhibit A-10 "
        "and following are Petitioner's photographs IMG_0442 through IMG_0534 (92 images) "
        "and the further photographs sent November 22, 2026 of the bedroom, closet, kitchen, "
        "cat property, tools, and living room. Additional photographs may be added before "
        "the hearing.",
    )
    pdf.ln(8)
    pdf.set_font("Times", "", 11)
    pdf.cell(0, 6, "Respectfully submitted,", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.cell(0, 6, "_________________________________", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Nyera Eldomiaty, Petitioner, Pro Se", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "eldomiatyn@yahoo.com", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Address and phone confidential, on file with the District Clerk", new_x="LMARGIN", new_y="NEXT")
    pdf.output(path)


if __name__ == "__main__":
    build_order("/workspace/hearing_packet/Proposed_Order_on_Motion_for_New_Trial.pdf")
    build_exhibit("/workspace/hearing_packet/Exhibit_A_Property_List.pdf")
    print("ok")
