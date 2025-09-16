from flask import Flask, request, render_template_string, redirect, url_for, flash
errors.append("Legal name is required.")
if not POSTAL_REGEX.match(data["postal_code"]):
errors.append("Postal code must be exactly 5 digits.")
if not data["order_date"]:
errors.append("Order date is required.")
if not data["amount"]:
errors.append("Purchase amount is required.")
else:
try:
float(data["amount"])
except ValueError:
errors.append("Purchase amount must be a number.")
if not data["currency"]:
errors.append("Currency is required.")


if data["payment_method"] == "Other" and not data["payment_other"]:
errors.append("Please specify the payment method.")
if data["card_country"] == "Other" and not data["card_country_other"]:
errors.append("Please specify the card issuance country.")


if errors:
for e in errors:
flash(e)
return redirect(url_for('index'))


mail_to = os.environ.get("MAIL_TO", "anca@outpostnow.com")
smtp_host = os.environ.get("SMTP_HOST")
smtp_port = int(os.environ.get("SMTP_PORT", "587"))
smtp_user = os.environ.get("SMTP_USER")
smtp_pass = os.environ.get("SMTP_PASS")


subject = "New Mexico Order Intake Form Submission"
text_lines = [
"SECTION 1 – Your details:",
f"Email: {data['email']}",
f"RFC: {data['rfc']}",
f"Legal Name: {data['legal_name']}",
f"Fiscal Regime Code: {data['fiscal_regime']}",
f"Postal Code: {data['postal_code']}",
f"UsoCFDI: {data['uso_cfdi']}",
"",
"SECTION 2 – Your order:",
f"Order Date: {data['order_date']}",
f"Purchase Amount: {data['amount']}",
f"Currency: {data['currency']}",
f"Payment Method: {data['payment_other'] if data['payment_method']=='Other' else data['payment_method']}",
f"Card Issuance Country: {data['card_country_other'] if data['card_country']=='Other' else data['card_country']}"
]
body_text = "\n".join(text_lines)


msg = MIMEMultipart()
msg['From'] = smtp_user or 'noreply@outpostnow.com'
msg['To'] = mail_to
msg['Subject'] = subject
msg.attach(MIMEText(body_text, 'plain', 'utf-8'))


try:
if not (smtp_host and smtp_user and smtp_pass):
raise RuntimeError("SMTP credentials missing. Set SMTP_HOST/SMTP_PORT/SMTP_USER/SMTP_PASS.")
with smtplib.SMTP(smtp_host, smtp_port) as server:
server.starttls()
server.login(smtp_user, smtp_pass)
server.send_message(msg)
except Exception as e:
flash(f"Submission saved, but email failed to send: {e}")
return render_template_string(SUCCESS_TEMPLATE)


return render_template_string(SUCCESS_TEMPLATE)




if __name__ == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
