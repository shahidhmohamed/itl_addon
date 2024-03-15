import requests
from xml.etree import ElementTree as ET
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _name = 'lbx_mi_gpo_i001'
    _description = 'Purchase Orders'

    order_number = fields.Char(string='Order Number')
    order_lines = fields.One2many('lbx_mi_gpo_i001.line', 'order_id', string='Order Lines')

    @api.model
    def store_decoded_data(self, order_number):
        # Define the SOAP request payload
        soap_request = f"""
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pod="http://sap.com/podown/">
                <soapenv:Header/>
                <soapenv:Body>
                    <pod:getPO>
                        <PO>{order_number}</PO>
                        <Frdt>01.01.2020</Frdt>
                        <Todt>31.12.2099</Todt>
                        <IUser>V_PoornimaJa</IUser>
                        <IPass>ITL@$OE@2o23</IPass>
                        <MerName>Jeewan Dissanayake</MerName>
                        <MerEmail>JeewanD@masholdings.com</MerEmail>
                        <Rev></Rev>
                        <system>PDM300</system>
                    </pod:getPO>
                </soapenv:Body>
            </soapenv:Envelope>
        """

        # URL for the SOAP web service
        soap_url = 'https://nwportal.masholdings.com/POXMLDownload/Config1?wsdl'

        # Make the SOAP request
        response = requests.post(soap_url, data=soap_request, headers={'Content-Type': 'text/xml'})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            try:
                # Parse the SOAP response
                xml_response = ET.fromstring(response.text)

                # Continue with the rest of your code
                return xml_response  # Return the parsed XML response
            except ET.ParseError as e:
                print(f"Error parsing SOAP response: {e}")
                return None
        else:
            print(f"SOAP request failed with status code: {response.status_code}")
            return None

    @api.model
    def perform_additional_action(self):
        xml_response = self.store_decoded_data(self.order_number)  # Pass the order_number as an argument

        if xml_response:
            order_lines_values = []
            for line in xml_response.findall('.//your_xml_path_to_order_lines'):
                # Extract data from XML and create a dictionary
                line_data = {
                    'order_number': line.find('.//PurchaseOrderNumber').text,
                    # 'field2': line.find('.//field2').text,
                    # Add other fields as needed based on your lbx_mi_gpo_i001.line model
                }
                order_lines_values.append((0, 0, line_data))

            # Append new lines to existing order_lines
            self.order_lines = order_lines_values

    # Define the button to trigger the action
    def button_fetch_purchase_order_data(self):
        self.perform_additional_action()
