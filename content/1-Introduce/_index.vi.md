---
title : "Giới thiệu"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

**Streaming Analytics** là giải pháp AWS để thu thập, lưu trữ và xử lý dữ liệu thời gian thực từ nhiều nguồn khác nhau. Trong workshop này, chúng ta sẽ áp dụng nó vào kịch bản **quản lý hàng tồn kho cửa hàng và điều phối giao hàng**.

Mỗi cửa hàng gửi dữ liệu hàng tồn kho sản phẩm của mình thông qua **StoreApp** vào **Amazon Kinesis Data Firehose**, ứng dụng này streaming dữ liệu đến **S3 bucket** để lưu trữ. Người dùng sau đó sẽ **thủ công gọi một Lambda function** (StorePlanningApp) để truy vấn dữ liệu bằng **Amazon Athena**, phân tích mức hàng tồn kho, và phát hiện những cửa hàng nào đang thiếu các sản phẩm cụ thể. Kết quả sau đó sẽ được gửi qua **Amazon SQS** để thông báo cho **StoreTruckApp**, ứng dụng điều phối xe tải giao hàng để bổ sung hàng hóa.

### Ưu điểm của phương pháp này
So với các phương pháp quản lý hàng tồn kho truyền thống, AWS Streaming Analytics mang lại một số lợi ích:

- **Giám sát hàng tồn kho thời gian thực** với lưu trữ data lake thay vì chờ đợi các báo cáo định kỳ
- **Xử lý Lambda serverless** với phân tích Athena, loại bỏ nhu cầu quản lý server hoặc cơ sở dữ liệu
- **Thu thập dữ liệu có thể mở rộng qua Kinesis Data Firehose**, có khả năng xử lý dữ liệu từ hàng trăm cửa hàng đồng thời
- **Hàng đợi tin nhắn đáng tin cậy với SQS**, đảm bảo các tin nhắn điều phối giao hàng không bị mất
- **Phân tích hiệu quả về chi phí**, bạn chỉ trả tiền cho dữ liệu được xử lý và các truy vấn được thực thi
- **Lưu trữ dữ liệu linh hoạt trong S3**, cho phép phân tích lịch sử và khả năng machine learning

### Tích hợp Các Thành phần Kiến trúc
- **StoreApp**: Thu thập và streaming dữ liệu hàng tồn kho từ các địa điểm bán lẻ
- **Kinesis Data Firehose**: Thu thập dữ liệu streaming một cách đáng tin cậy đến S3 với khả năng tự động mở rộng
- **S3 Consumption Zone**: Phục vụ như một data lake cho các bản ghi hàng tồn kho
- **Amazon Athena**: Cung cấp phân tích SQL serverless trên dữ liệu S3
- **StorePlanningApp (Lambda)**: Xử lý phân tích hàng tồn kho và kích hoạt cảnh báo
- **Amazon SQS**: Quản lý hàng đợi tin nhắn điều phối giao hàng
- **StoreTruckApp**: Giám sát SQS và điều phối xe tải giao hàng

Với những thành phần tích hợp này, hệ thống Streaming Analytics cho phép quản lý chuỗi cung ứng hiệu quả hơn, giảm rủi ro thiếu hàng tồn kho, cải thiện điều phối giao hàng, và nâng cao sự hài lòng tổng thể của khách hàng thông qua khả năng cung cấp hàng tồn kho tốt hơn.