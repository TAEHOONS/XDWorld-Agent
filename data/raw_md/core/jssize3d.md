---
description: 지도 내 크기와 관련된 기능을 관리하기 위한 API 입니다.
---

# JSSize3D

> Module.JSSize3D() API를 생성합니다.

```javascript
let width = 300;
let height = 200;
let scale = 1.0;

let size0 = new Module.JSSize3D();
let size1 = new Module.JSSize3D(width, height);
let size2 = new Module.JSSize3D(width, height, scale);
```

## properties

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| width  | number | 너비.       |
| height | number | 높이.       |
| depth  | number | 깊이.       |
