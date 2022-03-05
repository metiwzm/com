from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events, sync, Button
import asyncio, json, os
# ============= #
if not "unknown.json" in os.listdir():
	with open("unknown.json","w") as i:
		data = {"groups":[],"text":"First"}
		json.dump(data,i)
# ============= #
api_id, api_hash = 2591609, "dbe01607cc2d434e3b94dc0a85c8c9c7" # اینجا api_hash و api_id بزارید
unknown = TelegramClient("unknown", api_id, api_hash)
unknown.start()

@unknown.on(events.NewMessage())
async def comment(event):
	me = await unknown.get_me()
	if "change" in event.raw_text:
		if event.sender_id == me.id:
			try:
				with open("unknown.json") as r:
					v = json.load(r)
				split_text = event.raw_text.split("/")[1]
				if str(split_text) != v['text']:
					v['text'] = str(split_text)
					with open("unknown.json","w") as f:
						json.dump(v,f)
					await event.edit(f"〽️ متن ' {split_text} ' با موفقیت جایگزین متن قبلی شد")
				else:
						await event.edit("❌ متن قبلی با متن داده شده مطابقت دارد ، لطفا متن جدیدی وارد کنید")
			except:
				await event.edit("➖ نوع استفاده از دستور اشتباه است")
						
				
	elif "add" in event.raw_text:
		if event.sender_id == me.id:
			try:
				with open("unknown.json","r") as c:
					x = json.load(c)
				split_text = event.raw_text.split()[1]
				if int(split_text) not in x['groups']:
					x["groups"].append(int(split_text))
					with open("unknown.json","w") as o:
						json.dump(x,o)
					await event.edit("⚠️ کانال باموفقیت به لیست افزوده شد")
				else:
					await event.edit("🔅 ایدی عددی از قبل در لیست وجود دارد")
			except:
				await event.edit("➖ نوع استفاده از دستور اشتباه است")
	elif event.raw_text == "stat":
		if event.sender_id == me.id:
			with open("unknown.json") as e:
				x = json.load(e)
			lists = str()
			if len(x['groups']) != 0:
				ted = len(x['groups'])
				ta = "✅"
				kar = "دارید"
				unknown.parse_mode = 'html'
				for o in x['groups']:
					lists += f"🆔 : <code>{o}</code>\n"
			else:
				ta = "❌"
				kar = "ندارید"
			try:
				texx = x["text"]
				await event.edit(f"""🔆 وضعیت ربات شما :
	{ta} شما {ted} ایدی عددی در دیتابیس {kar}
	📝 متن کامنت : {texx}
	〰〰〰〰〰〰〰〰〰
	{lists}""")
			except:
				await event.edit(f"""🔆 وضعیت ربات شما :
	{ta} شما ایدی عددی در دیتابیس {kar}
	📝 متن کامنت : {texx}
	〰〰〰〰〰〰〰〰〰
	{lists}""")
	elif "adlist" in event.raw_text:
		if event.sender_id == me.id:
			x = event.raw_text.find("(")+1
			x1 = event.raw_text.find(")")
			real = event.raw_text[x:x1].split()
			with open("unknown.json") as z:
				n = json.load(z)
			rep = str()
			for j in real:
				if not int(j) in n['groups']:
					rep += "🆔 "+str(j)+"\n"
					n['groups'].append(int(j))
				else:
					rep += f"❌ کانال {j} قبلا ثبت شده\n"
				with open("unknown.json","w") as c:
					json.dump(n,c)
				await event.edit(f"""💯 لیست کانال ها به دیتابیس افزوده شد.
	کانال های دریافتی👇🏻
	
	{rep}""")

	elif event.raw_text == 'delAll':
		if event.sender_id == me.id:
			with open("unknown.json") as t:
				k = json.load(t)
			k['groups'] = list()
			with open("unknown.json","w") as c:
				json.dump(k,c)
			await event.edit("🏷 لیست ایدی عددی کانالها باموفقیت پاکسازی شد")
	elif event.raw_text == "meti":
		unknown.parse_mode = 'html'
		await event.edit("""💢 راهنمای ربات کامنت اول:

📌 دستور <b>change</b> :
شما با این دستور میتونید متن کامنت رو عوض کنید ، متن کامنت اول بصورت پیشفرض First است و شما میتونید به این صورت متن رو عوض کنید!
🔸 مثال :
<code>change / TEXT</code>
بجای TEXT متن مورد نظر رو بنویسید.

📌 دستور <b>adlist<b/> :
شما با این دستور میتونید لیستی از کانال هارو توی دیتابیس ذخیره کنید
🔸 مثال :
<code>adlist (-100467000 -1002456 -10023540)</code>

📌 دستور <b>delAll</b> :
شما با این دستور میتونید لیست ایدی عددی های ثبت شده در دیتابیس رو پاکسازی کنید
🔸 مثال :
<code>delAll</code>

📌 دستور <b>add</b> :
شما با این دستور میتونید ایدی عددی کانالی که میخواید کامنت اول براش بزارید رو به دیتابیس اضافه کنید
ایدی عددی کانالی که میخواید اضافه کنید حتما باید اولش 100- باشه
❗️ نکته :
شما باید در گپ متصل به اون کانال عضو باشید تا بتونید کامنت اول رو بگیرید!
🔸 مثال :
<code>add -100111111111</code>

📌 دستور <b>del</b> :
شما با این دستور میتونید فقط یک ایدی عددی ثبت شده رو از دیتابیس حذف کنید
🔸 مثال :
<code>del -100111111111</code>

📌 دستور <b>stat</b> :
شما میتونید با این دستور وضعیت ربات خودتون رو ببینید
اطلاعاتی از قبیل : تعداد ایدی عددی های ثبت شده و ایدی عددی های ثبت شده در دیتابیس
🔸 مثال :
<code>stat</code>
〰〰〰〰〰〰〰〰〰〰
منبع :
🔸 @PythonVirus

🔺 <b>توجه</b> :
هرگونه اسکی بدون ذکر منبع پیگرد قانونی و شخصی در پی خواهد داشت""")
	elif "del" in event.raw_text:
		if event.sender_id == me.id:
			try:
				with open("unknown.json") as e:
					c = json.load(e)
				split_text = event.raw_text.split()[1]
				if int(split_text) in c['groups']:
					c['groups'].remove(int(split_text))
					with open("unknown.json","w") as b:
						json.dump(c,b)
					await event.edit("🗑 ایدی عددی با موفقیت از لیست حذف شد")
				else:
					await event.edit("🗃 همچین ایدی عددی در لیست وجود ندارد")
			except:
				await event.edit("➖ نوع استفاده از دستور اشتباه است")
	with open("unknown.json") as i:
		x = json.load(i)
	if event.sender_id in x['groups']:
		if event.chat_id not in x['groups']:
			await event.reply(str(x['text']))


unknown.run_until_disconnected()
asyncio.get_event_loop().run_forever()