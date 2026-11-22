#!/usr/bin/env python3
"""Build proposed order and Exhibit A PDFs for 25-12729-393."""

from fpdf import FPDF

from exhibit_a_items import SECTIONS


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


def emit_items(pdf, start_n, items):
    n = start_n
    pdf.set_font("Times", "", 10)
    for text_item in items:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5, f"{n}. {text_item}")
        n += 1
    return n


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
        "Other rooms: dresser, mirror, clothing, bags, bathroom products, hair tools, kitchen, "
        "pantry, living room, and personal effects shown in Petitioner's photographs, and "
        "any other property of Petitioner in the residence. Petitioner claims the white GE "
        "washer, the white GE dryer, and both bidets. Apartment-installed stove, refrigerator, "
        "shower fixtures, tub, toilet bowls, and apartment door hardware are not claimed.",
    )
    body(
        pdf,
        "This list names each object visible in the photographs. It does not group bottles, "
        "tubes, jars, cases, or tools under a single label. Where a brand is readable, the "
        "brand is stated. Where a label is not readable, the object is still listed by "
        "color, shape, or container. Counts on clothing-bag labels are Petitioner's counts.",
    )
    n = 1
    for section_title, items in SECTIONS:
        heading(pdf, section_title)
        n = emit_items(pdf, n, items)
        pdf.ln(1)
    heading(pdf, "Category awards requested")
    cats = [
        "A. All of Petitioner's clothing, shoes, jewelry, and personal effects at Respondent's residence, whether or not separately photographed, including every labeled bag and box in the closet photographs.",
        "B. All furniture and household goods belonging to Petitioner at Respondent's residence, including the dresser, bed and white bedding, pair of nightstands, lamp, desks, office chair, dining table and chairs, tufted bench, area rugs, sofas, marble-look coffee table, glass coffee table, poufs, full-length wood-framed floor mirror, black-framed wall mirror, carved-wood cabinet, nested console tables, folding tray table, whiteboard and rolling easel, metal etagere, mirrored side tables, laundry sorter, rolling shoe rack, media console, green shelves, brackets and screws, green marble slab, television mount, robot vacuum, white GE washer, white GE dryer, both bidets, and any other furniture, furnishings, or household items that are Petitioner's.",
        "C. Every personal-care bottle, tube, jar, compact, brush, hair tool, hair product, facial device, and medication belonging to Petitioner, including each object listed above. This category is not a single grouped label.",
        "D. Kitchenware belonging to Petitioner: Dutch oven, KitchenAid stand mixer, espresso/coffee machine, toaster oven, SodaStream, air fryer, hand mixer, silverware, cooking utensils, blender, All-Clad pans, bakeware, food storage, dishes, glassware, kettles, pantry food that is Petitioner's, and small appliances. Built-in or apartment-installed stove, refrigerator, shower fixtures, tub, toilet bowls, and apartment door hardware are not claimed.",
        "E. Petitioner's cat and all pet-related property, including the automatic litter box, orange covered litter box, chrome cat tree or shelf frame, toys, bowls, veterinary records, microchip registration, medications, food, litter, carriers, and supplies.",
        "F. Petitioner's records and identity documents, including legal, identification, immigration, medical, financial, tax, insurance, employment, family, and sentimental records; books packed in the Living Room box; every notebook, journal, notepad, and handwritten note; and the videos, course files, and study recordings of what Petitioner learned over the years.",
        "G. Phones, computers, tablets, both MacBook Pros, monitor, printer, keyboard, chargers, drives, DeWalt tools, and digital accounts and contents belonging to Petitioner, including every file, note, photo, and video on those devices.",
        "H. All other personal property belonging to Petitioner at Respondent's residence or in Respondent's possession.",
    ]
    for line in cats:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", "", 11)
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
        "dryer, phone, blood-pressure cuff, clothing, bags, and bathroom products. Exhibit A-10 "
        "and following are Petitioner's photographs IMG_0442 through IMG_0534 (92 images), "
        "the further photographs sent November 22, 2026 of the bedroom, closet, kitchen, "
        "cat property, tools, and living room, untitled folder 7 (110 photographs), "
        "New Folder With Items (121 photographs), and Archive.zip (98 unique photographs "
        "of the packed home, dated September 16, 2026). Additional photographs may be added "
        "before the hearing.",
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
